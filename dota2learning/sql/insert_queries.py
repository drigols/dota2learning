# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


insert_into_hero_table = """
  INSERT INTO hero
  (
    id,
    name,
    localized_name,
    primary_attr,
    attack_type,
    img,
    icon,
    base_health,
    base_health_regen,
    base_mana,
    base_mana_regen,
    base_armor,
    base_attack_min,
    base_attack_max,
    base_str,
    base_agi,
    base_int,
    str_gain,
    agi_gain,
    int_gain,
    attack_range,
    projectile_speed,
    move_speed,
    legs
  )
  VALUES
  (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s
  );
"""
