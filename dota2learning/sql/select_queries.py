# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
from __future__ import annotations


get_names_query = """
SELECT name, localized_name FROM hero WHERE id=%s
"""
