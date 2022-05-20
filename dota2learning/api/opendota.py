# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


import requests
import json

from .urls import HEROES_STATS_URL


def get_heroes_stats():
  try:
    response = requests.get(f"{HEROES_STATS_URL}")
  except Exception as error:
    return print("You have problem to get Heroes Stats: ", error)
  else:
    heroes = json.loads(response.text)
    return heroes
