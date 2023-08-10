import markdown
import pathlib
from ._wikilinks import PensieveLinkExtension
from ._headings import HeadingExtension

import textwrap

TEMPLATE = textwrap.dedent(
    """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {contents}
    </body>
    </html>
"""
)


def render(path: pathlib.Path, template=None):
    if template is None:
        template = TEMPLATE

    # make the path absolute
    path = pathlib.Path(path).resolve()

    with path.open() as fileobj:
        contents = fileobj.read()

    md = markdown.markdown(
        contents,
        extensions=[
            "codehilite",
            "def_list",
            "fenced_code",
            "admonition",
            "footnotes",
            "smarty",
            "toc",
            PensieveLinkExtension(),
            HeadingExtension(),
        ],
    )

    print(
        template.format(
            contents=md,
            title=path.parent.name,
            path=(path.parent.parent.name + "/" + path.parent.name),
        )
    )
