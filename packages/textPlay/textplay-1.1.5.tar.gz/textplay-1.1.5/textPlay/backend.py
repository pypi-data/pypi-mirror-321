"""
# Backend module for executing commands in the background and handling errors.

Functions:
 - subProcess(command: str) -> Optional[subprocess.CompletedProcess]:
 - suppress(command: str) -> None:
 - osExecute(command: str) -> int:
"""

import os
import subprocess
from typing import Optional, Union

def subProcess(command: str) -> Optional[subprocess.CompletedProcess]:
    """
    Executes the given command in the background using the subprocess module.

    Parameters:
    - command (str): The command to be executed.

    Returns:
    - subprocess.CompletedProcess: If the command executes successfully.
    - None: If an error occurs.

    Raises:
    - subprocess.CalledProcessError: If the command returns a non-zero exit status.

    Example:
    >>> result = backend_subprocess("echo 'Hello, World!'")
    >>> if result:
    >>>     print(result.stdout)
    """
    try:
        result = subprocess.run(
            command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr.strip()}", flush=True)
        return None

def suppress(command: str) -> None:
    """
    Executes the given command in the background and suppresses its output.

    Parameters:
    - command (str): The command to be executed.

    Example:
    >>> backend_suppress("echo 'Hello, World!'")

    Output:
    (No output is displayed)
    """
    try:
        with open(os.devnull, "w") as devnull:
            subprocess.check_call(command, shell=True, stdout=devnull, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Error suppressing command: {e}", flush=True)

def osExecute(command: str) -> int:
    """
    Executes the given command in the background and waits for it to complete.

    Parameters:
    - command (str): The command to be executed.

    Returns:
    - int: The exit code of the executed command.

    Example:
    >>> exit_code = backend_exec("echo 'Hello, World!'")
    >>> print(f"Command exited with code: {exit_code}")
    """
    try:
        return os.system(command)
    except Exception as e:
        print(f"Error executing command: {e}", flush=True)
        return 1


