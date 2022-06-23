# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

import json

import requests

from dota2learning.api.urls import HEROES_STATS_URL


def get_heroes_stats() -> list:
    """Get Heroes stats from OpenDota API.
        URL: https://api.opendota.com/api/heroStats

    Returns:
        list: The return is a list of dictionaries,
        where each hero is a dictionary contain hero's stats.
    """
    try:
        response = requests.get(f"{HEROES_STATS_URL}")
    except Exception as error:
        print("You have problem to get Heroes Stats:", error)
    else:
        heroes_stats = []
        temp = []
        heroes = json.loads(response.text)
        for hero in range(len(heroes)):
            temp.append(heroes[hero]["id"])
            temp.append(heroes[hero]["name"])
            temp.append(heroes[hero]["localized_name"])
            temp.append(heroes[hero]["primary_attr"])
            temp.append(heroes[hero]["attack_type"])
            temp.append("https://api.opendota.com" + heroes[hero]["img"])
            temp.append("https://api.opendota.com" + heroes[hero]["icon"])
            temp.append(heroes[hero]["base_health"])
            temp.append(heroes[hero]["base_health_regen"])
            temp.append(heroes[hero]["base_mana"])
            temp.append(heroes[hero]["base_mana_regen"])
            temp.append(heroes[hero]["base_armor"])
            temp.append(heroes[hero]["base_attack_min"])
            temp.append(heroes[hero]["base_attack_max"])
            temp.append(heroes[hero]["base_str"])
            temp.append(heroes[hero]["base_agi"])
            temp.append(heroes[hero]["base_int"])
            temp.append(heroes[hero]["str_gain"])
            temp.append(heroes[hero]["agi_gain"])
            temp.append(heroes[hero]["int_gain"])
            temp.append(heroes[hero]["attack_range"])
            temp.append(heroes[hero]["projectile_speed"])
            temp.append(heroes[hero]["move_speed"])
            temp.append(heroes[hero]["legs"])
            heroes_stats.append(temp)
            temp = []
        return heroes_stats
