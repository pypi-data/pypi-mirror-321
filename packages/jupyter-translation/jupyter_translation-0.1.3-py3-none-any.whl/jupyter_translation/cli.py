"""Entry point for the Jupyter notebook translation CLI."""

import asyncio

import typer
from typing_extensions import Annotated

from .translate import translate_single_notebook


app = typer.Typer()


@app.command()
def translate_notebook(
    input_path: str,
    output_path: Annotated[
        str,
        typer.Option(help="The name of output jupyter notebook file."),
    ] = "",  # no Union[str, None] because typer doesn't support it
    *,
    src_lang: Annotated[
        str, typer.Option(help="The language used in the input path.")
    ] = "fr",
    dest_lang: Annotated[
        str,
        typer.Option(
            help="The language used to translate the input path into the output path."
        ),
    ] = "en",
) -> None:
    asyncio.run(
        translate_single_notebook(
            input_path, output_path, src_lang=src_lang, dest_lang=dest_lang
        )
    )


if __name__ == "__main__":
    app()
