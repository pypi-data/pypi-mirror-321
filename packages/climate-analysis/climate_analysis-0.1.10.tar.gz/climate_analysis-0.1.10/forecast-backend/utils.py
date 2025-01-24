# SPDX-FileCopyrightText: 2024 Deutscher Wetterdienst
#
# SPDX-License-Identifier: EUPL-1.2

from collections.abc import Sequence
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path
from subprocess import PIPE, CalledProcessError, CompletedProcess, run
from typing import List, Literal, TypedDict, Sequence, cast

from evaluation_system.misc import logger


def mkdirs(path: Path) -> None:
    """Create a directory with correct permissions."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        path.chmod(0o775)
    except Exception as e:
        logger.error(f"Failed to create directory {path}: {e}")
        raise


def call_process(script: str, error_file: Path, *args: Sequence[str]) -> None:
    """Call an external process and log the output."""
    command = script.split(" ") + list(args)
    logger.info(f"Running command: {' '.join(command)}")
    try:
        with error_file.open("w") as error_f:
            run(command, check=True, stderr=error_f)

    except CalledProcessError as e:
        logger.error(
            f"Command '{' '.join(command)}' failed with exit code {e.returncode}.\n"
            f"Traceback: {error_file.read_text()}"
        )
        raise SystemExit(e.returncode)


class KwargsDict(TypedDict):
    stderr: int
    check: bool
    text: Literal[True]


def call_process_parallel(
    script: Path,
    error_file: Path,
    n_proc: int,
    input_iterable: Sequence[str],
    *args,
):
    """
    Run a batch of subprocesses in parallel, defined by a script and a list of inputs.

    Args:
        script (Path): Path to the script to be executed.
        error_file (Path): Path to an error file where stderr is written to.
        n_proc (int): Maximum number of processes (threads) spawned in parallel.
        input_iterable (list[str]): The list of inputs to be processed in parallel.

    Raises:
        SystemExit: If any subprocess spawned encounters an error, this error is raised with the error code of the encountered error.
    """
    with ThreadPoolExecutor(n_proc) as executor:
        # Schedule tasks for given script, input that is iterated over, and any fixed args
        logger.info(
            f"Running script {script} in parallel for arguments {input_iterable} and fixed args {*args, }."
        )
        threads: List[Future] = []
        for input in input_iterable:
            argv = [script, input, *args]
            kwargs: KwargsDict = {"stderr": PIPE, "check": True, "text": True}
            future: Future = executor.submit(run, argv, **kwargs)
            threads.append(future)
        # Check results of tasks, raise error in case any task fails
        with error_file.open("w") as errf:
            returncode = 0
            stderr: str
            for future in threads:
                try:
                    result: CompletedProcess = future.result()
                    stderr = result.stderr
                except CalledProcessError as e:
                    stderr = e.stderr
                    returncode = e.returncode
                if stderr:
                    errf.write(stderr)
        if returncode != 0:
            logger.error(f"Encountered error: {error_file.read_text()}")
            raise SystemExit(returncode)
