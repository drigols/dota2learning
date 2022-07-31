# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HeroModel(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    localized_name = Column(VARCHAR(50), nullable=False)
    primary_attr = Column(VARCHAR(50), nullable=False)
    attack_type = Column(VARCHAR(50), nullable=False)
    img = Column(VARCHAR(100), nullable=False)
    icon = Column(VARCHAR(100), nullable=False)
    base_health = Column(Float, nullable=False)
    base_health_regen = Column(Float, nullable=False)
    base_mana = Column(Float, nullable=False)
    base_mana_regen = Column(Float, nullable=False)
    base_armor = Column(Float, nullable=False)
    base_attack_min = Column(Float, nullable=False)
    base_attack_max = Column(Float, nullable=False)
    base_str = Column(Float, nullable=False)
    base_agi = Column(Float, nullable=False)
    base_int = Column(Float, nullable=False)
    str_gain = Column(Float, nullable=False)
    agi_gain = Column(Float, nullable=False)
    int_gain = Column(Float, nullable=False)
    attack_range = Column(Float, nullable=False)
    projectile_speed = Column(Float, nullable=False)
    move_speed = Column(Float, nullable=False)
    legs = Column(Integer, nullable=False)


fakeHeroInsert = {
    "id": 500,
    "name": "Drigols",
    "localized_name": "drigols_RMG",
    "primary_attr": "Agility",
    "attack_type": "Range",
    "img": "www.google.com.br",
    "icon": "www.google.com.br",
    "base_health": 1.5,
    "base_health_regen": 1.5,
    "base_mana": 1.5,
    "base_mana_regen": 1.5,
    "base_armor": 1.5,
    "base_attack_min": 1.5,
    "base_attack_max": 1.5,
    "base_str": 1.5,
    "base_agi": 1.5,
    "base_int": 1.5,
    "str_gain": 1.5,
    "agi_gain": 1.5,
    "int_gain": 1.5,
    "attack_range": 1.5,
    "projectile_speed": 1.5,
    "move_speed": 1.5,
    "legs": 2,
}
