import markdown
import pathlib
from ._wikilinks import PensieveLinkExtension

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

    with path.open() as fileobj:
        contents = fileobj.read()

    md = markdown.markdown(
        contents,
        extensions=[
            "admonition",
            "codehilite",
            "def_list",
            "fenced_code",
            "footnotes",
            "smarty",
            "toc",
            PensieveLinkExtension(),
        ],
    )

    print(template.format(contents=md, title=path.parent.name))
