""" colors

This file is part of Turtle.

Turtle is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Turtle is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Turtle. If not, see <https://www.gnu.org/licenses/>. 
"""
import gi
gi.require_version("Adw", "1")
from gi.repository import Adw

THEME_COLORS = [
    # TODO use theme specific colors
    # these are colors from the GNOME color palette
    (98, 160, 234),
    (87, 227, 137),
    (248, 228, 92),
    (255, 163, 72),
    (237, 51, 59),
    (192, 97, 203),
    (181, 131, 90),
]

THEME_COLORS_DARK = [
    # TODO use theme specific colors
    # these are colors from the GNOME color palette
    (26, 95, 180),
    (38, 162, 105),
    (229, 165, 10),
    (198, 70, 0),
    (165, 29, 45),
    (97, 53, 131),
    (99, 69, 44),
]

def get_theme_colors():
    """ get theme colors depending on dark or light theme"""
    style_manager = Adw.StyleManager()
    colors = THEME_COLORS_DARK if style_manager.get_dark() else THEME_COLORS

    return colors

def get_theme_color_by_index(index):
    """ get color hex string of a theme color defined in THEME_COLORS """
    colors = get_theme_colors()

    if index < len(colors):
        (red, green, blue) = colors[index]
        color = "#%02x%02x%02x" % (red, green, blue)
        return color

    return "blue"
