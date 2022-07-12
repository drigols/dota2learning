# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from pydantic import BaseModel


class HeroSchema(BaseModel):
    id: int
    name: str
    localized_name: str
    primary_attr: str
    attack_type: str
    img: str
    icon: str
    base_health: float
    base_health_regen: float
    base_mana: float
    base_mana_regen: float
    base_armor: float
    base_attack_min: float
    base_attack_max: float
    base_str: float
    base_agi: float
    base_int: float
    str_gain: float
    agi_gain: float
    int_gain: float
    attack_range: float
    projectile_speed: float
    move_speed: float
    legs: int

    class Config:
        orm_mode = True
