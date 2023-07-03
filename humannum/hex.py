#
# MIT License
#
# Copyright (c) 2023 nbiotcloud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Hexadecimal."""

from .baseint import BaseInt


class Hex(BaseInt, int):  # type: ignore
    """
    Integer with hexadecimal representation.

    >>> Hex(50)
    0x32
    >>> Hex(500)
    0x1F4

    This hexadecimal value behaves like a normal integer.

    >>> 8 + Hex(8)
    16
    >>> Hex(8) + 8
    0x10
    >>> Hex(8) - 2
    0x6
    >>> Hex(8) * 3
    0x18
    >>> Hex(8) / 3
    0x2
    >>> Hex(8) // 3
    0x2
    >>> Hex(8) % 5
    0x3
    >>> Hex(8) << 1
    0x10
    >>> Hex(8) >> 1
    0x4
    >>> Hex(8) ** 2
    0x40
    >>> Hex(9) & 3
    0x1
    >>> Hex(8) | 3
    0xB
    >>> Hex(9) ^ 3
    0xA
    >>> divmod(Hex(9), 3)
    (0x3, 0x0)
    >>> ~Hex(9)
    -0xA
    >>> -Hex(9)
    -0x9
    >>> abs(Hex(-9))
    0x9
    >>> +Hex(9)
    0x9

    >>> Hex(8) | 'A'
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for |: 'Hex' and 'str'
    >>> divmod(Hex(9), 'A')
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for divmod(): 'Hex' and 'str'

    Corner Cases:

    >>> Hex(0)
    0x0
    >>> Hex(-5)
    -0x5

    Width:

    >>> a = Hex(3)
    >>> a
    0x3
    >>> a.width=6
    >>> a
    0x03

    >>> a = Hex(-3)
    >>> a
    -0x3
    >>> a.width=6
    >>> a
    -0x03
    """

    def __repr__(self):
        value = int(self)
        try:
            width = self.width
        except AttributeError:
            width = None
        # pylint: disable=consider-using-f-string
        if width:
            pat = "0x%%0%dX" % ((width + 3) / 4,)
        else:
            pat = "0x%X"
        if value >= 0:
            return pat % (value,)
        return ("-" + pat) % (-value,)

    __str__ = __repr__
