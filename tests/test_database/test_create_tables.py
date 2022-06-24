# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import pytest

from dota2learning.database.create_tables import create_table
from dota2learning.sql.create_table import hero_table
from dota2learning.sql.create_table import invalid_table


@pytest.mark.create_table
def test_create_table_invalid_query():
    """Testing the create_table() function returns False
    when there is an invalid SQL query."""
    result = create_table(invalid_table)
    assert result is False


@pytest.mark.create_table
def test_create_table_is_true():
    """Test whether function create_table() returns True
    after it can create the table."""
    result = create_table(hero_table)
    assert result is True
