from __future__ import annotations

project = "Engineering Blueprint"
author = "Amalie Shi"
release = "1.0"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {".md": "markdown"}

html_theme = "furo"
html_title = "Engineering Blueprint"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1a5276",
        "color-brand-content": "#1a5276",
    },
    "dark_css_variables": {
        "color-brand-primary": "#5dade2",
        "color-brand-content": "#5dade2",
    },
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]

myst_heading_anchors = 3

exclude_patterns = [
    "_build",
    ".venv",
    "README.md",   # GitHub-facing document; not part of the Sphinx site
    "CLAUDE.md",   # AI assistant config; not user-facing documentation
]
