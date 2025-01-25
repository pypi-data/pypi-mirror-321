"""Tests for the translate module."""

import pytest
import nbformat
from jupyter_translation.translate import (
    translate_single_notebook,
    translate_multiple_notebooks,
)
from jupyter_translation.errors import NumberArgumentError


@pytest.mark.parametrize(
    "input_path, output_path, src_lang, dest_lang",
    [
        ("test_notebook.ipynb", "translated_notebook.ipynb", "fr", "en"),
        ("test_notebook.ipynb", "", "fr", "en"),
    ],
)
@pytest.mark.asyncio
async def test_translate_single_notebook(mocker, input_path, output_path, src_lang, dest_lang):
    # Create a mock notebook
    nb = nbformat.v4.new_notebook()
    nb.cells.append(nbformat.v4.new_markdown_cell("Bonjour"))
    nb.cells.append(nbformat.v4.new_code_cell("# Commentaire"))
    nb.cells.append(nbformat.v4.new_code_cell("print('Hello')"))

    mock_open = mocker.patch("builtins.open", new_callable=mocker.MagicMock)
    mocker.patch("nbformat.read", return_value=nb)
    mocker.patch("nbformat.write")
    mock_translate = mocker.patch(
        "googletrans.Translator.translate", new_callable=mocker.AsyncMock
    )

    mock_translate.side_effect = lambda text, src, dest: mocker.AsyncMock(
        text="Hello" if text == "Bonjour" else "# Comment"
    )

    await translate_single_notebook(
        input_path, output_path, src_lang=src_lang, dest_lang=dest_lang
    )

    mock_open.assert_called()
    mock_translate.assert_any_call("Bonjour", src=src_lang, dest=dest_lang)
    mock_translate.assert_any_call("# Commentaire", src=src_lang, dest=dest_lang)


@pytest.mark.asyncio
async def test_translate_multiple_notebooks(mocker):
    input_files = ["test_notebook1.ipynb", "test_notebook2.ipynb"]
    src_lang = "fr"
    dest_lang = "en"

    mock_translate_single = mocker.patch(
        "jupyter_translation.translate.translate_single_notebook",
        new_callable=mocker.AsyncMock,
    )

    await translate_multiple_notebooks(
        *input_files, src_lang=src_lang, dest_lang=dest_lang
    )

    assert mock_translate_single.call_count == len(input_files)
    for input_file in input_files:
        mock_translate_single.assert_any_call(
            input_file, src_lang=src_lang, dest_lang=dest_lang
        )


@pytest.mark.asyncio
async def test_translate_multiple_notebooks_no_files():
    with pytest.raises(NumberArgumentError):
        await translate_multiple_notebooks()
