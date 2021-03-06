# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import typer

from dota2learning.database.get_from_database import (
    get_hero_names_from_database,
)

app = typer.Typer(help="Commands for getting Heroes attributes and insights.")


@app.command()
def get_names(id: int):
    """Get hero names by ID from the Database.

    Args:
        id (int): Hero ID.
    """
    hero_names = get_hero_names_from_database(id)
    typer.echo(hero_names)
