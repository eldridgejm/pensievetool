import argparse
import sys
import pathlib

from . import render as _render


def cmd_render(args):
    _render.render(args.path, args.template)


def path_reader(path):
    with path.open() as fileobj:
        return fileobj.read()

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    render_parser = subparsers.add_parser("render")
    render_parser.set_defaults(command=cmd_render)
    render_parser.add_argument("path", type=pathlib.Path, help="Path to markdown note.")
    render_parser.add_argument(
        "template",
        type=path_reader,
        default=None,
        nargs="?",
        help="Path to HTML that will be used as the template.",
    )

    args = parser.parse_args()
    if not hasattr(args, "command"):
        parser.print_help()
        sys.exit(1)

    args.command(args)
