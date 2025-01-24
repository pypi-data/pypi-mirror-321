"""
Copyright (c) 2025-now Martian Bugs All rights reserved.
Build Date: 2025-01-16
Author: Martian Bugs
Description: 字体解密
"""

import unicodedata
from contextlib import suppress

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph

FONT_First_Point_Coordinates = [
    (42, 348),
    (356, 709),
    (129, 458),
    (218, 333),
    (419, 709),
    (470, 697),
    (286, 381),
    (509, 697),
    (130, 200),
    (409, 472),
]
"""字体的第一笔的坐标, 自上而下分别是 0/1/2/.../9"""


class FontDecrypter:
    def __init__(self, font_path: str):
        self.font_path = font_path
        self.font_mapping = self.getFontUnicodeMap(font_path=self.font_path)

    def getFontUnicodeMap(self, font_path: str):
        """
        获取字体 Unicode 与实际值的映射关系

        Args:
            font_path: 字体路径
        Returns:
            字体 Unicode 与实际值的映射关系
        """

        font = TTFont(font_path)
        glyph_names: list[str] = font.getGlyphNames()
        glyph_names = [name for name in glyph_names if name.startswith('uni')]

        glyf_table = font['glyf']

        mapping: dict[str, int] = {}
        for name in glyph_names:
            glyph: Glyph = glyf_table[name]
            coordinates, _, _ = glyph.getCoordinates(glyf_table)
            try:
                unicode_str = chr(int(name[3:], 16))
                mapping[unicode_str] = FONT_First_Point_Coordinates.index(
                    coordinates[0]
                )
            except ValueError:
                continue

        font.close()
        return mapping

    def decrypt(self, text: str):
        """
        文本解密

        Args:
            text: 待解密文本
        Returns:
            解密后的文本
        """

        if not self.font_mapping:
            raise ValueError('字体映射表为空, 请先获取字体映射表')

        result: list[str] = []

        for char in text:
            with suppress(ValueError, TypeError):
                unicodedata.name(char)
                result.append(char)
                continue

            char_value = self.font_mapping.get(char)
            if char_value is None:
                result.append(char)
            else:
                result.append(str(char_value))

        return ''.join(result)
