# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import typer

from dota2learning.cli import hero

app = typer.Typer()

app.add_typer(hero.app, name="hero")
