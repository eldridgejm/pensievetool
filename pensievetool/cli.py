import argparse
import sys
import pathlib

from . import render as _render
from . import index as _index


def cmd_render(args):
    print(_render.render(args.path, args.template))


def cmd_index(args):
    print(_index.index(args.path, args.template, reverse=args.descending))


def path_reader(path):
    path = pathlib.Path(path)
    with path.open() as fileobj:
        return fileobj.read()


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    render_parser = subparsers.add_parser("render")
    render_parser.set_defaults(command=cmd_render)
    render_parser.add_argument("path", type=pathlib.Path, help="Path to markdown note.")
    render_parser.add_argument(
        "--template",
        type=path_reader,
        default=None,
        help="Path to HTML that will be used as the template.",
    )

    index_parser = subparsers.add_parser("index")
    index_parser.set_defaults(command=cmd_index)
    index_parser.add_argument(
        "path", type=pathlib.Path, help="Path to directory to index."
    )
    index_parser.add_argument(
        "--descending", action="store_true", help="Sort in descending order."
    )
    index_parser.add_argument(
        "--template",
        type=path_reader,
        default=None,
        help="Path to HTML that will be used as the template.",
    )

    args = parser.parse_args()
    if not hasattr(args, "command"):
        parser.print_help()
        sys.exit(1)

    args.command(args)
