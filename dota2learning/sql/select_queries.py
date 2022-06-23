# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT


get_names_query = """
SELECT name, localized_name FROM hero WHERE id=%s
"""
