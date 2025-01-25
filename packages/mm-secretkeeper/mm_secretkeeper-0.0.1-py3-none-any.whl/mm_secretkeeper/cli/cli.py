import getpass
from typing import Annotated

import pyperclip
import typer
from mm_std import hr, print_json, print_plain

from mm_secretkeeper.cli import daemon
from mm_secretkeeper.http_server import run_http_server

BASE_URL = "http://localhost:3000"

app = typer.Typer(no_args_is_help=True, pretty_exceptions_enable=False, add_completion=False)


@app.command(name="start")
def start_command(daemonize: Annotated[bool, typer.Option("-d")] = True) -> None:
    port = 3000
    if daemonize:
        daemon.start(port)
    else:
        run_http_server(port)


@app.command("stop")
def stop_command() -> None:
    daemon.stop()


@app.command(name="lock")
def lock_command() -> None:
    res = hr(f"{BASE_URL}/lock", method="POST")
    print_json(res.json)


@app.command(name="unlock")
def unlock_command() -> None:
    password = getpass.getpass()
    res = hr(f"{BASE_URL}/unlock", method="POST", params={"password": password}, json_params=False)
    print_json(res.json)


@app.command(name="health")
def health_command() -> None:
    res = hr(f"{BASE_URL}/health")
    print_json(res.json)


@app.command(name="list")
def list_command() -> None:
    res = hr(f"{BASE_URL}/list")
    if res.json.get("keys") and not res.json.get("error"):
        for k in res.json["keys"]:
            print_plain(k)
    else:
        print_json(res.json)


@app.command(name="get")
def get_command() -> None:
    key = input("key: ")
    res = hr(f"{BASE_URL}/get", method="POST", params={"key": key}, json_params=False)
    if res.json.get("value"):
        value = res.json.get("value")
        print_plain(value)
        pyperclip.copy(value)
    else:
        print_json(res.json)


@app.command(name="add")
def add_command() -> None:
    key = input("key: ")
    value = getpass.getpass("value")
    res = hr(f"{BASE_URL}/add", method="POST", params={"key": key, "value": value})
    print_json(res.json)


@app.command(name="delete")
def delete_command() -> None:
    key = input("key: ")
    res = hr(f"{BASE_URL}/delete", method="POST", params={"key": key}, json_params=False)
    print_json(res.json)


if __name__ == "__main__":
    app()
