# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import pytest
from typer.testing import CliRunner

from dota2learning.cli.main import app


runner = CliRunner()


@pytest.mark.get_names
def test_get_names_stdout_id_1():
    """Test if output console is hero id=1."""
    result = runner.invoke(app, ["hero", "get-names", "91"])
    assert result.exit_code == 0
    assert (
        result.stdout
        == "{'name': 'npc_dota_hero_wisp', 'localized_name': 'Io'}\n"
    )


@pytest.mark.get_names
def test_get_names_invalid_id():
    """Test the console return when pass invalid id,
    that's, no hero with this ID."""
    result = runner.invoke(app, ["hero", "get-names", "500"])
    assert result.exit_code == 0
    assert result.stdout == "There is no hero with this ID.\n\n"
