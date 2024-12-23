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

def do_move(maze, cannon):
    limit = len(maze[0])

    walls = set()

    for row in maze:
        for cell in row:
            if cell["type"] == "wall":
                walls.add((cell["x"], cell["y"]))

    diff = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (1, -1), (-1, 1),
        (1, 1), (-1, -1)
    ]

    best_result = []

    for d_x, d_y in diff:
        walls_hit = []
        c_x, c_y = cannon[0] + d_x, cannon[1] + d_y

        while c_x > -1 and c_x <= limit and c_y > -1 and c_y <= limit:
            if (c_x, c_y) in walls:
                walls_hit.append((c_x, c_y))
            
            c_x += d_x
            c_y += d_y
        
        if len(walls_hit) > len(best_result):
            best_result = walls_hit
    
    return best_result