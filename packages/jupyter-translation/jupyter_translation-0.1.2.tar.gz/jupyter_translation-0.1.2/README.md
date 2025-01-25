# JUPYTER-TRANSLATION

**Translate your Jupyter notebooks from the command line or in a Python script.**

[![PyPI Version](https://img.shields.io/pypi/v/jupyter-translation?color=%2334D058&label=pypi%20package)](https://pypi.org/project/jupyter-translation/)
[![License MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/numgrade/stringstyler/blob/main/LICENSE)
![Python 3](https://img.shields.io/badge/Python%20version-3.9%2B-blue)

--

## Installation

Create and activate a virtual environment and then install jupyter-translation:

```console
$ pip install jupyter-translation

---> 100%
```

## Usage

### jupyter-translation in the command line

$ jupyter-translation input_notebook.ipynb

It translates input_notebook.ipynb from French to English. The result is a file named input_notebook_en.ipynb.

Get help with this command :

$ jupyter-translation --help


### jupyter-translation in a Python script

```python

import asyncio

from jupyter_translation.translate import translate_notebook


# Translate one notebook from Spanish to English.
asyncio.run(
        translate_single_notebook(
            input_files="input_notebook.ipynb", 
            output_path="translated_notebook.ipynb",
            src_lang='es',
            dest_lang='en'
            )
    )

# Translate multiple notebooks. Default translation is from French to English.
asyncio.run(translate_multiple_notebooks("input_notebook1.ipynb", "input_notebook2.ipynb"))
```


## License

This project is licensed under the terms of the MIT license.