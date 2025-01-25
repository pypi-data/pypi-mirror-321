"""
This markdown processor borrows heavily from facelessuser/pymdown-extensions

https://github.com/facelessuser/pymdown-extensions/tree/main
"""

import markdown
import markdown.util
import markdown.blockprocessors
import markdown.inlinepatterns
import re

import xml.etree.ElementTree as etree

import markdown_latex_prerender.render

# fuck you etree, why do I have to do this????
etree.register_namespace("", "http://www.w3.org/2000/svg")


_RE_SMART_DOLLAR_INLINE = (
    r"(?:(?<!\\)((?:\\{2})+)(?=\$)|(?<!\\)(\$)(?!\s)((?:\\.|[^\\$])+?)(?<!\s)(?:\$))"
)
_RE_DOLLAR_INLINE = (
    r"(?:(?<!\\)((?:\\{2})+)(?=\$)|(?<!\\)(\$)((?:\\.|[^\\$])+?)(?:\$)))"
)
_RE_BRACKET_INLINE = (
    r"(?:(?<!\\)((?:\\{2})+?)(?=\\\()|(?<!\\)(\\\()((?:\\[^)]|[^\\])+?)(?:\\\)))"
)

_RE_DOLLAR_BLOCK = r"((?P<dollar>[$]{2})(?P<math>((?:\\.|[^\\])+?))(?P=dollar))"
_RE_TEX_BLOCK = (
    r"((?P<math2>\\begin\{(?P<env>[a-z]+\*?)\}(?:\\.|[^\\])+?\\end\{(?P=env)\}))"
)
_RE_BRACKET_BLOCK = r"(\\\[(?P<math3>(?:\\[^\]]|[^\\])+?)\\\])"


def _strip_namespace(element: etree.Element) -> etree.Element:
    """Recursively remove namespaces from an ElementTree element."""
    for elem in element.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]  # Remove the namespace
        for attr in tuple(elem.attrib):
            if "}" in attr:
                elem.attrib[attr.split("}", 1)[1]] = elem.attrib.pop(attr)
    return element


def _render_math_to_svg(math, classes: list[str]) -> etree.Element:
    """Convert math expression to etree element"""

    svg = markdown_latex_prerender.render.render_latex(math, "")
    el = etree.fromstring(svg)
    el = _strip_namespace(el)
    el.attrib["class"] = " ".join((*classes, *el.attrib.get("class", "").split(" ")))
    el.attrib["alt"] = math
    el.attrib["title"] = math
    return el


class InlineLatexPattern(markdown.inlinepatterns.InlineProcessor):
    """
    inline pattern handler for latex replacements.
    """

    ESCAPED_BSLASH = "{}{}{}".format(markdown.util.STX, ord("\\"), markdown.util.ETX)

    def __init__(self, pattern, config):
        super().__init__(pattern)

    def handleMatch(
        self, m: re.Match[str], data
    ) -> tuple[str | etree.Element, int, int]:
        """Handle notations and switch them to something that will be more detectable in HTML."""

        # Handle escapes
        groups = m.groups()
        escapes = groups[0]
        if not escapes and len(groups) > 3:
            escapes = groups[3]
        if escapes:
            return escapes.replace("\\\\", self.ESCAPED_BSLASH), m.start(0), m.end(0)

        # Handle Tex
        math = groups[2]
        if not math and len(groups) > 3:
            math = groups[5]

        return (
            _render_math_to_svg(math, ("latex-inline", "latex")),
            m.start(0),
            m.end(0),
        )


class BlockLatexProcessor(markdown.blockprocessors.BlockProcessor):
    def __init__(self, pattern, config, md):
        """Initialize."""
        self.match = None
        self.pattern = re.compile(pattern, re.DOTALL | re.UNICODE)

        super().__init__(md.parser)

    def test(self, parent, block):
        """Return 'True' for future Python Markdown block compatibility."""
        self.match = self.pattern.match(block)
        return self.match is not None

    def mathjax_output(self, parent, math: str):
        """Default MathJax output."""

        grandparent = parent
        parent = etree.SubElement(grandparent, "figure", {"class": "latex-figure"})

        svg_el = _render_math_to_svg(math.strip(), ("latex-block", "latex"))

        parent.append(svg_el)

        return svg_el

    def run(self, parent, blocks):
        """Find and handle block content."""

        blocks.pop(0)

        groups = self.match.groupdict()
        math = groups.get("math", "")
        if not math:
            math = groups.get("math2", "")
        if not math:
            math = groups.get("math3", "")

        self.mathjax_output(parent, math)

        return True


class LatexExtension(markdown.Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            "smart_dollar": [True, "Use Arithmatex's smart dollars - Default True"],
            "block_syntax": [
                ["dollar", "square", "begin"],
                'Enable block syntax: "dollar" ($$...$$), "square" (\\[...\\]), and '
                '"begin" (\\begin{env}...\\end{env}). - Default: ["dollar", "square", "begin"]',
            ],
            "inline_syntax": [
                ["dollar", "round"],
                'Enable inline syntax: "dollar" ($$...$$), "bracket" (\\(...\\)) '
                ' - Default: ["dollar", "round"]',
            ],
        }

        super().__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        """Extend the inline and block processor objects."""

        md.registerExtension(self)
        md.ESCAPED_CHARS = md.ESCAPED_CHARS + ["$"]

        config = self.getConfigs()

        # Inline patterns
        allowed_inline = set(config.get("inline_syntax"))
        smart_dollar = config.get("smart_dollar")
        inline_patterns = []
        if "dollar" in allowed_inline:
            inline_patterns.append(
                _RE_SMART_DOLLAR_INLINE if smart_dollar else _RE_DOLLAR_INLINE
            )
        if "round" in allowed_inline:
            inline_patterns.append(_RE_BRACKET_INLINE)
        if inline_patterns:
            inline = InlineLatexPattern("|".join(inline_patterns), config)
            md.inlinePatterns.register(inline, "latex-inline", 189.9)

        # Block patterns
        allowed_block = set(config.get("block_syntax"))
        block_patterns = []
        if "dollar" in allowed_block:
            block_patterns.append(_RE_DOLLAR_BLOCK)
        if "square" in allowed_block:
            block_patterns.append(_RE_BRACKET_BLOCK)
        if "begin" in allowed_block:
            block_patterns.append(_RE_TEX_BLOCK)
        if block_patterns:
            block = BlockLatexProcessor(
                "(?s)^(?:{})[ ]*$".format("|".join(block_patterns)), config, md
            )
            md.parser.blockprocessors.register(block, "latex-block", 79.9)
