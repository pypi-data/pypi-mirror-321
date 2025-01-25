"""
A Sphinx extension to add markdown generation support.
"""

from sphinx_markdown_builder.builder import MarkdownBuilder

__version__ = "0.6.8"
__docformat__ = "reStructuredText"


def setup(app):
    app.add_builder(MarkdownBuilder)
    app.add_config_value("markdown_http_base", "", "html")
    app.add_config_value("markdown_uri_doc_suffix", ".md", "html")
    app.add_config_value("markdown_anchor_sections", False, "html")
    app.add_config_value("markdown_anchor_signatures", False, "html")
    app.add_config_value("markdown_docinfo", False, "html")
    app.add_config_value("markdown_bullet", "*", "html")
