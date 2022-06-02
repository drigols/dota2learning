# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import pytest

from dota2learning.database import get_connection
from dota2learning.database import close_connection
from dota2learning.database import get_hero_names_from_database


@pytest.mark.connections
def test_get_connection():
    """Test if database connects with default parameters."""
    result = get_connection()
    assert bool(result) == True


@pytest.mark.connections
def test_get_connection_invalid_database():
    """Test if the return is None when pass invalid name from database."""
    result = get_connection(database_name="dotalearning")
    assert result == None


@pytest.mark.connections
def test_close_connection():
    """Test if the connection is closed, that's, False."""
    connection = get_connection()
    result = close_connection(connection)
    assert bool(result) == True


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
