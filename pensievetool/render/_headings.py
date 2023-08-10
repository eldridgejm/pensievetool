"""Distinguishes special headings, like :Topics: and :Thoughts:"""

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree import ElementTree as etree


class HeadingTreeprocessor(Treeprocessor):
    def run(self, root):
        headings = root.findall("h1")
        for heading in headings:
            if heading.text is None:
                continue

            if heading.text.startswith(":") and heading.text.endswith(":"):
                title = heading.text.strip(":").capitalize()

                open = etree.Element("span")
                open.text = ":"
                open.set("class", "colon")

                title_span = etree.Element("span")
                title_span.text = title

                close = etree.Element("span")
                close.text = ":"
                close.set("class", "colon")

                heading.text = ""
                heading.extend([open, title_span, close])
                heading.set("class", "special")


class HeadingExtension(Extension):
    def extendMarkdown(self, md):
        self.md = md

        # append to end of inline patterns
        heading_processor = HeadingTreeprocessor()
        md.treeprocessors.register(heading_processor, "heading", 1)
