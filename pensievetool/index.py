import textwrap
import pathlib


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


def index(path: pathlib.Path, template=None, reverse=True):
    """Render an index of all the notes in a directory."""
    if template is None:
        template = TEMPLATE

    # make a list of the directories in `path`
    entries = sorted(path.iterdir(), reverse=reverse)
    directories = [d for d in entries if d.is_dir()]

    def make_link(d):
        return f'<li><a class="wikilink" href="{d.name}/note.html">{d.name}</a></li>'

    links = "\n".join(make_link(d) for d in directories)
    page = template.format(title=path.name, contents=f"<ul>{links}</ul>")
    return page
