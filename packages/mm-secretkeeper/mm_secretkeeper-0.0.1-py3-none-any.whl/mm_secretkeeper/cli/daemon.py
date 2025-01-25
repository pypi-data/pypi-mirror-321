import os
from pathlib import Path

import daemon
import typer
from daemon import pidfile

from mm_secretkeeper.http_server import run_http_server

PID_FILE = Path("/tmp/mm-secret-keeper.pid")  # nosec
STDOUT_FILE = Path("/tmp/mm-secret-keeper-stdout.log")  # nosec
STDERR_FILE = Path("/tmp/mm-secret-keeper-stderr.log")  # nosec


def start(port: int) -> None:
    typer.echo("Starting the sk daemon...")
    with daemon.DaemonContext(
        working_directory="/",
        pidfile=pidfile.TimeoutPIDLockFile(PID_FILE),
        stdout=open(STDOUT_FILE, "w+"),
        stderr=open(STDERR_FILE, "w+"),
    ):
        run_http_server(port)


def stop() -> None:
    """Stop the daemon process."""
    if PID_FILE.exists():
        with open(str(PID_FILE)) as pid_file:
            pid = int(pid_file.read().strip())
        try:
            os.kill(pid, 15)  # Send SIGTERM signal
            typer.echo(f"Daemon process (PID {pid}) terminated.")
        except ProcessLookupError:
            typer.echo("Process not found.")
        PID_FILE.unlink()  # Remove the PID file
    else:
        typer.echo("Daemon is not running (PID file not found).")
