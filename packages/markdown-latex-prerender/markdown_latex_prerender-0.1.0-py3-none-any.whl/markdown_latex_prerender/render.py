import subprocess
import tempfile
import os

_latex_template = r"""\documentclass{{minimal}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{xcolor}}
{preamble}

\begin{{document}}
\[
{tex}
\]
\end{{document}}"""


def render_latex(snippet: str, preamble: str) -> str | None:
    """
    converts a latex snippet, together with some preamble (macros, etc.)
    to an inline svg string
    """
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, "input.tex"), "w") as f:
                f.write(_latex_template.format(preamble=preamble, tex=snippet))
            r = subprocess.run(
                [
                    "dvilualatex",
                    "--no-shell-escape",
                    "--no-socket",
                    "--halt-on-error",
                    "input.tex",
                ],
                cwd=tmpdir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            # make sure everything went ok:
            if not r.returncode == 0:
                print(
                    "failed at:\n"
                    + _latex_template.format(preamble=preamble, tex=snippet)
                )
                return f'<span class="latex-error">{r.stdout.read().decode().replace('&', '&amp;').replace('<', '&lt;')}</span>'

            res = subprocess.check_output(
                ["dvisvgm", "--no-fonts", "-O", "-Z", "1.5", "input.dvi", "-s"],
                cwd=tmpdir,
                stderr=subprocess.DEVNULL,
                text=True,
            )
            # skip everything until the svg starts:
            return res[res.index("<svg ") :]
    except subprocess.CalledProcessError as err:
        raise err
        return None
