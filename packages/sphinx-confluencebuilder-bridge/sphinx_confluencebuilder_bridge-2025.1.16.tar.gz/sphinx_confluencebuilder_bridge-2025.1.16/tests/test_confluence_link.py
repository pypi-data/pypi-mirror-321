"""
Tests for the ``:confluence_link:`` role.
"""

import json
from collections.abc import Callable
from pathlib import Path
from textwrap import dedent

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test_confluence_link(
    tmp_path: Path,
    make_app: Callable[..., SphinxTestApp],
) -> None:
    """
    The ``:confluence_link:`` role renders like a normal link.
    """
    source_directory = tmp_path / "source"
    source_directory.mkdir()

    conf_py = source_directory / "conf.py"
    conf_py_content = dedent(
        text="""\
        extensions = [
            "sphinxcontrib.confluencebuilder",
            "sphinx_confluencebuilder_bridge",
        ]
        """,
    )
    conf_py.write_text(data=conf_py_content)

    source_file = source_directory / "index.rst"
    index_rst_template = dedent(
        text="""\
            {link}
            """,
    )

    confluencebuilder_directive_source = dedent(
        text="""\
            :confluence_link:`https://www.bbc.co.uk`
            """,
    )

    docutils_directive_source = dedent(
        text="""\
            `https://www.bbc.co.uk <https://www.bbc.co.uk>`_
            """,
    )

    source_file.write_text(
        data=index_rst_template.format(
            link=confluencebuilder_directive_source,
        ),
    )

    app = make_app(srcdir=source_directory)
    app.build()
    assert app.statuscode == 0
    assert not app.warning.getvalue()

    confluencebuilder_directive_html = (app.outdir / "index.html").read_text()
    app.cleanup()

    source_file.write_text(
        data=index_rst_template.format(link=docutils_directive_source),
    )
    app = make_app(srcdir=source_directory)
    app.build()
    assert app.statuscode == 0
    assert not app.warning.getvalue()

    docutils_directive_html = (app.outdir / "index.html").read_text()

    assert confluencebuilder_directive_html == docutils_directive_html


def test_linkcheck(
    tmp_path: Path,
    make_app: Callable[..., SphinxTestApp],
) -> None:
    """
    Links are checked by the ``linkcheck`` builder.
    """
    source_directory = tmp_path / "source"
    source_directory.mkdir()

    conf_py = source_directory / "conf.py"
    conf_py_content = dedent(
        text="""\
        extensions = [
            "sphinxcontrib.confluencebuilder",
            "sphinx_confluencebuilder_bridge",
        ]

        confluence_bridge_users = {
            "eloise.red": "1234a",
        }

        confluence_server_url = "https://example.com/wiki"
        """,
    )
    conf_py.write_text(data=conf_py_content)

    source_file = source_directory / "index.rst"
    index_rst_content = dedent(
        text="""\
            :confluence_link:`https://badlink.example.com`

            `https://badlink2.example.com <https://badlink2.example.com>`_
            """,
    )

    source_file.write_text(data=index_rst_content)

    app = make_app(srcdir=source_directory, buildername="linkcheck")
    app.build()
    assert not app.warning.getvalue()
    assert app.statuscode != 0
    output_json_lines = (app.outdir / "output.json").read_text().splitlines()
    expected_num_errors = 2
    assert len(output_json_lines) == expected_num_errors
    for line in output_json_lines:
        output_data = json.loads(s=line)
        assert output_data["status"] == "broken"
