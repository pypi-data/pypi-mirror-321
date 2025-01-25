"""This module provides functionality to translate Jupyter notebooks from one language to another
using the Google Translate API.
Functions:
    translate_notebook(input_path, output_path, src_lang='fr', dest_lang='en'):
        Translates the content of a Jupyter notebook from the source language to the destination language.
        Translates both markdown cells and comments within code cells.
Example usage:
    translate_notebook('input_notebook.ipynb', 'translated_notebook.ipynb')
"""

import asyncio
from pathlib import Path

from googletrans import Translator
import nbformat
from rich import print

from jupyter_translation.errors import NumberArgumentError


async def translate_single_notebook(
    input_path: str,
    output_path: str = "",
    *,
    src_lang: str = "fr",
    dest_lang: str = "en",
) -> None:
    """Translates the content of a single Jupyter notebook from the source language to the destination language.

    Args:
        input_path (str): The path to the input Jupyter notebook file.
        output_path (str): The path to save the translated Jupyter notebook file.
        src_lang (str): The source language code (default is 'fr' for French).
        dest_lang (str): The destination language code (default is 'en' for English).

    Returns:
        None
    """
    print(f"Translating notebook {input_path}...")
    with open(input_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    async with Translator() as translator:
        # Translate each cell
        for cell in nb.cells:
            if cell.cell_type == "markdown":
                cell.source = await translator.translate(
                    cell.source, src=src_lang, dest=dest_lang
                )
                cell.source = cell.source.text
            elif cell.cell_type == "code":
                # Translate comments in code cells
                lines = cell.source.split("\n")
                translated_lines = []
                for line in lines:
                    if line.strip().startswith("#"):
                        translated_line = await translator.translate(
                            line, src=src_lang, dest=dest_lang
                        )
                        translated_lines.append(translated_line.text)
                    else:
                        translated_lines.append(line)
                cell.source = "\n".join(translated_lines)

    # Save the translated notebook
    if not output_path:
        path = Path(input_path)
        output_path = f"{path.stem}_{dest_lang}{path.suffix}"
    print(
        f"Saving translated notebook [bold blue]{input_path}[/bold blue] to [bold blue]{output_path}[/bold blue]. "
        f"The original language was [bold green]'{src_lang}'[/bold green]. "
        f"The translated language is [bold green]'{dest_lang}'[/bold green]."
    )
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print("[bold red]Translation complete![/bold red] :tada: :tada: :tada:")


async def translate_multiple_notebooks(
    *input_files: str,
    src_lang: str = "fr",
    dest_lang: str = "en",
) -> None:
    """Translates the content of multiple Jupyter notebooks from the source language to the destination language.

    Args:
        input_files (str): One or several paths to the input Jupyter notebook files.
        src_lang (str): The source language code (default is 'fr' for French).
        dest_lang (str): The destination language code (default is 'en' for English).

    Returns:
        None
    """
    if not input_files:
        raise NumberArgumentError("At least one input file must be provided.")

    for input_path in input_files:
        await translate_single_notebook(
            input_path, src_lang=src_lang, dest_lang=dest_lang
        )


if __name__ == "__main__":
    # Example usage
    asyncio.run(
        translate_single_notebook("input_notebook.ipynb", "translated_notebook.ipynb")
    )
    # Example usage with multiple input files
    asyncio.run(
        translate_multiple_notebooks("input_notebook1.ipynb", "input_notebook2.ipynb")
    )
    # Example that throws an error due to missing input files
    asyncio.run(translate_multiple_notebooks())
