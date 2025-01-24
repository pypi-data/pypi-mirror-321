import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--workdir", "-w", type=str, default=None, help="Path must be passed with dots in place of slashes")
parser.add_argument(
    "--script_path",
    "-s",
    type=str,
    default=None,
    help="Relative path to workdir. Must be separated with dots, without python extension",
)
parser.add_argument(
    "--port",
    "-p",
    type=int,
    default=8001,
    help="Port number to run the server on. Default is 8001",
)
parser.add_argument(
    "--host",
    "-h",
    type=str,
    default="0.0.0.0",
    help="Host to run the server on. Default is 0.0.0.0",
)


def get_args() -> dict:
    args = parser.parse_args()
    if not all([args.workdir, args.script_path]):
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    workdir = "/" + os.path.join(*args.workdir.split("."))

    rel_path = os.path.join(*args.script_path.split("."))
    script_path = os.path.join(workdir, rel_path) + ".py"

    return {"workdir": workdir, "script_path": script_path, "port": args.port, "host": args.host}
