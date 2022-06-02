# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import pytest

from dota2learning.api.opendota import get_heroes_stats


@pytest.mark.get_heroes_stats
def test_get_heroes_stats_is_list():
    """Test if get_heroes_stats() function returns is a list."""
    result = get_heroes_stats()
    assert type(result) is list


@pytest.mark.get_heroes_stats
def test_get_heroes_stats_list_is_empty():
    """Test if get_heroes_stats() function returns is a empty list."""
    result = get_heroes_stats()
    assert bool(result) == True
