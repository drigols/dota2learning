# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import typer

from dota2learning.database import get_hero_names_from_database

app = typer.Typer(help="Commands for getting Heroes attributes and insights.")


@app.command()
def get_names(id: int):
    """Get hero names by ID from the Database.

    Args:
        id (int): Hero ID.
    """
    hero_names = get_hero_names_from_database(id)
    typer.echo(hero_names)
