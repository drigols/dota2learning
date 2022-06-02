# -*- coding: utf-8 -*-
# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


test_table = """
CREATE TABLE d2_test (
  `id` INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL
);
"""

hero_table = """
CREATE TABLE IF NOT EXISTS `Hero` (
  `id` INT NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `localized_name` VARCHAR(50) NOT NULL,
  `primary_attr` VARCHAR(50) NOT NULL,
  `attack_type` VARCHAR(50) NOT NULL,
  `img` VARCHAR(100) NOT NULL,
  `icon` VARCHAR(100) NOT NULL,
  `base_health` FLOAT NOT NULL,
  `base_health_regen` FLOAT NOT NULL,
  `base_mana` FLOAT NOT NULL,
  `base_mana_regen` FLOAT NOT NULL,
  `base_armor` FLOAT NOT NULL,
  `base_attack_min` FLOAT NOT NULL,
  `base_attack_max` FLOAT NOT NULL,
  `base_str` FLOAT NOT NULL,
  `base_agi` FLOAT NOT NULL,
  `base_int` FLOAT NOT NULL,
  `str_gain` FLOAT NOT NULL,
  `agi_gain` FLOAT NOT NULL,
  `int_gain` FLOAT NOT NULL,
  `attack_range` FLOAT NOT NULL,
  `projectile_speed` FLOAT NOT NULL,
  `move_speed` INT NOT NULL,
  `legs` INT NOT NULL,
  PRIMARY KEY (`id`)
  );
"""