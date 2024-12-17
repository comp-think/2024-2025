# -*- coding: utf-8 -*-
# Copyright (c) 2019, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

from group import do_move

maze = [
    [
        {
            "x": 0,
            "y": 0,
            "type": "free"
        },
        {
            "x": 1,
            "y": 0,
            "type": "free"
        },
        {
            "x": 2,
            "y": 0,
            "type": "free"
        },
        {
            "x": 3,
            "y": 0,
            "type": "free"
        }
    ],
    [
        {
            "x": 0,
            "y": 1,
            "type": "free"
        },
        {
            "x": 1,
            "y": 1,
            "type": "wall"
        },
        {
            "x": 2,
            "y": 1,
            "type": "free"
        },
        {
            "x": 3,
            "y": 1,
            "type": "wall"
        }
    ],
    [
        {
            "x": 0,
            "y": 2,
            "type": "free"
        },
        {
            "x": 1,
            "y": 2,
            "type": "free"
        },
        {
            "x": 2,
            "y": 2,
            "type": "free"
        },
        {
            "x": 3,
            "y": 2,
            "type": "free"
        }
    ],
    [
        {
            "x": 0,
            "y": 3,
            "type": "wall"
        },
        {
            "x": 1,
            "y": 3,
            "type": "wall"
        },
        {
            "x": 2,
            "y": 3,
            "type": "free"
        },
        {
            "x": 3,
            "y": 3,
            "type": "free"
        }
    ]
]

cannon = (3, 3)

result = do_move(maze, cannon)

print("List of walls destroyed by the cannon:", result)