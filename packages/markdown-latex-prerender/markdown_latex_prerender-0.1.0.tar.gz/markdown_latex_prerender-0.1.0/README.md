# Markdown LaTeX Prerenderer

This is a very simple [python-markdown](https://github.com/Python-Markdown/markdown) extension, similar to other markdon-latex implementations that adds support
for latex in markdown files.

The key differences to other approaches are:

1. It does not require javascript on the client
2. It does not require nodejs when building

For some reason, I could not find a way to render latex inside a markdown file without Javascript, that seemed crazy to
me. So I built this tool. No KaTeX required. No NodeJS required. Just classic latex implementations.

## How to use:

Make sure you have `dvilualatex` and `dvisvgm` installed on your system.

Then, add `LatexExtension` to your markdown extension list:

```python
import markdown
from markdown_latex_prerender import LatexExtension

markdown.markdown(
    md_str,
    extensions=[
        LatexExtension(),
        ...
    ],
)
```

## How it works:

It uses the hosts `dvilualatex` and `dvisvgm` (both usually come with TexLive and friends) to convert a latex snippet to
an svg file. **It does not ship either program itself. This is why it's less that 200 lines of code.

Do not feed it untrusted input. It may break. Or worse.

## Caching:

You may want to cache rendered things. For this, you can do something like this:

```python
from my_fav_caching_library import cache_function

import markdown_latex_prerenderer.render as render

render.render_latex = cache_function(render.render_latex)
```

Or whatever else you feel like doing.

## Inpiration:

Since I don't know how to build a python-markdown module to render inline-latex, I ~~asked chatGPT~~ looked at other
peoples solutions. I found this: [arithmatex.py](https://github.com/facelessuser/pymdown-extensions/blob/main/pymdownx/arithmatex.py)
in [facelessuser/pymdown-extensions](https://github.com/facelessuser/pymdown-extensions/blob/main/pymdownx/arithmatex.py).
I re-used a lot of their code. I guess it works.
