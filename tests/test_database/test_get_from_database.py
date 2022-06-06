# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import pytest

from dota2learning.database.get_from_database import get_hero_names_from_database


@pytest.mark.get_names
def test_get_hero_names_from_database_id_1():
    """Test if the get_names() function return is a dictionary with names from hero id=1."""
    result = get_hero_names_from_database(1)
    assert result == {'name': 'npc_dota_hero_antimage', 'localized_name': 'Anti-Mage'}


@pytest.mark.get_names
def test_get_hero_names_from_database_invalid_id():
    """Test if the return is None when pass invalid ID, that's, no has Hero with this ID."""
    result = get_hero_names_from_database(500)
    assert result == None
