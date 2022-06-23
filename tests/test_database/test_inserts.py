# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import pytest

from dota2learning.database.inserts import insert_data_into_table
from dota2learning.sql.insert_queries import insert_into_hero_table
from dota2learning.api.opendota import get_heroes_stats


@pytest.mark.insert
def test_insert_data_into_hero_table_false():
    """Testing if the return is False when enter except block."""
    result = insert_data_into_table(insert_into_hero_table, get_heroes_stats())
    assert bool(result) is False
