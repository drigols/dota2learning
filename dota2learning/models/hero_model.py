# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import VARCHAR

from dota2learning.database.connection import Base


class HeroModel(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50))
    localized_name = Column(VARCHAR(50))
    primary_attr = Column(VARCHAR(50))
    attack_type = Column(VARCHAR(50))
    img = Column(VARCHAR(100))
    icon = Column(VARCHAR(100))
    base_health = Column(Float)
    base_health_regen = Column(Float)
    base_mana = Column(Float)
    base_mana_regen = Column(Float)
    base_armor = Column(Float)
    base_attack_min = Column(Float)
    base_attack_max = Column(Float)
    base_str = Column(Float)
    base_agi = Column(Float)
    base_int = Column(Float)
    str_gain = Column(Float)
    agi_gain = Column(Float)
    int_gain = Column(Float)
    attack_range = Column(Float)
    projectile_speed = Column(Float)
    move_speed = Column(Float)
    legs = Column(Integer)
