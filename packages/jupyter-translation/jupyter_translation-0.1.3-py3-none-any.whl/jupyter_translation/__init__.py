"""Init file for jupyter_translation package.

This file is used to define the package's public API.

The public API consists of the following functions:
- translate_single_notebook: A function to translate a single notebook.
- translate_multiple_notebooks: A function to translate multiple notebooks.

The __version__ variable is also defined in this file.
"""

import importlib.metadata
from .translate import translate_single_notebook, translate_multiple_notebooks  # noqa: F401


# Get the verson number from pyproject.toml / jupyter_translation.__version__
__version__ = importlib.metadata.version("jupyter_translation")