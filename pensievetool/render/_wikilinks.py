"""
PensieveLinks Extension for Python-Markdown
======================================

Converts [[PensieveLinks]] to relative links.

See <https://Python-Markdown.github.io/extensions/wikilinks>
for documentation.

Original code Copyright [Waylan Limberg](http://achinghead.com/).

All changes Copyright The Python Markdown Project

Additional modifications: Justin Eldridge

License: [BSD](https://opensource.org/licenses/bsd-license.php)

"""

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree

from .. import parse


def build_link(label, *_):
    """Build a URL from the label, a base, and an end."""
    parts = parse.parse_key(label)
    if parts.file is not None:
        if parts.name == ".":
            prefix = "."
        else:
            prefix = f"/{parts.type_}/{parts.name}"
        return f"{prefix}/{parts.file}", "filelink"
    else:
        url = f"/{parts.type_}/{parts.name}/note.html"
        html_class = "wikilink"
        return url, html_class


class PensieveLinkExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {}
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        # append to end of inline patterns
        WIKILINK_RE = r"\[\[([\w0-9_ \-():\./]+)\]\]"
        wikilinkPattern = PensieveLinksInlineProcessor(WIKILINK_RE, self.getConfigs())
        wikilinkPattern.md = md
        md.inlinePatterns.register(wikilinkPattern, "wikilink", 75)


class PensieveLinksInlineProcessor(InlineProcessor):
    def __init__(self, pattern, config):
        super().__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        if m.group(1).strip():
            label = m.group(1).strip()
            url, html_class = build_link(label)
            span = etree.Element("span")
            span.set('class', html_class)

            openbr = etree.Element("span")
            openbr.text = '[['
            openbr.set('class', 'wikilinkbracket')

            closebr = etree.Element("span")
            closebr.text = ']]'
            closebr.set('class', 'wikilinkbracket')

            a = etree.Element("a")
            a.text = label
            a.set("href", url)
            if html_class:
                a.set("class", html_class)

            span.append(openbr)
            span.append(a)
            span.append(closebr)
        else:
            span = ""
        return span, m.start(0), m.end(0)


def makeExtension(**kwargs):  # pragma: no cover
    return PensieveLinkExtension(**kwargs)
