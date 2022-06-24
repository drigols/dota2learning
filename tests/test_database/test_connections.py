# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import pytest

from dota2learning.database.connections import close_connection
from dota2learning.database.connections import get_connection


@pytest.mark.connections
def test_get_connection():
    """Testing if database connects with default parameters."""
    result = get_connection()
    assert bool(result) is True


@pytest.mark.connections
def test_get_connection_invalid_database():
    """Testing if the return is None when
    pass invalid name from database."""
    result = get_connection(database_name="dotalearning")
    assert result is None


@pytest.mark.connections
def test_close_connection_true():
    """Testing if the connection is closed, that's, True."""
    connection = get_connection()
    result = close_connection(connection)
    assert result is True


@pytest.mark.connections
def test_close_connection_false():
    """Testing if the return is False when
    function receive closed connection."""
    connection = get_connection(database_name="dotalearning")
    result = close_connection(connection)
    assert result is False
