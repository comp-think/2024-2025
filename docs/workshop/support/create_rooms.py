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

from random import shuffle, choice
from networkx import Graph, NetworkXError, shortest_path
from collections import defaultdict
from argparse import ArgumentParser
from os import makedirs
from os.path import exists, sep
from json import dump

def get_edge_cells(set_of_cells, edge_size):
    result = defaultdict(list)

    for x, y in set_of_cells:
        if 0 <= x < edge_size - 1 and y == 0:
            result["top"].append((x, y))
        elif x == 0 and 1 <= y < edge_size:
            result["left"].append((x, y))
        elif 0 < x < edge_size and y == edge_size - 1:
            result["bottom"].append((x, y))
        elif x == edge_size - 1 and 0 <= y < edge_size - 1:
            result["right"].append((x, y))
    
    return result


def find_cannon(rooms):
    result = None

    limit = len(rooms[0])

    room_list = []
    walls = set()
    for row in rooms:
        for room in row:
            room_list.append(room)
            if room["type"] == "wall":
                walls.add((room["x"], room["y"]))        

    while result is None:
        cell = choice(room_list)
        cannon = cell["x"], cell["y"]

        diff = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (1, -1), (-1, 1),
            (1, 1), (-1, -1)
        ]

        for d_x, d_y in diff:
            c_x, c_y = cannon[0] + d_x, cannon[1] + d_y

            while c_x > -1 and c_x <= limit and c_y > -1 and c_y <= limit:
                if (c_x, c_y) in walls:
                    return cannon

                c_x += d_x
                c_y += d_y


def get_number_of_cells(total, p_free, p_wall):
    n_free = round((total / 100) * p_free)
    n_wall = round((total / 100) * p_wall)

    diff = total - (n_free + n_wall)
    while diff != 0:
        if diff > 0:
            val = 1
            diff -= 1
        else:
            val = -1
            diff += 1
        n_free += val
    
    return n_free, n_wall

def create_board(edge_size, p_free, p_wall):
    free, wall = get_number_of_cells(edge_size * edge_size, p_free, p_wall)
    cell_list = free * ["free"] + wall * ["wall"]
    shuffle(cell_list)

    structure = []
    for y in range(edge_size):
        row = []
        for x in range(edge_size):
            cell = cell_list.pop(0)
            row.append({
                "x": x,
                "y": y,
                "type": cell
            })
        structure.append(row)
                
    cannon = find_cannon(structure)

    return {
        "structure": structure,
        "cannon":{
            "x": cannon[0],
            "y": cannon[1]
        }
    }

if __name__ == "__main__":
    arg_parser = ArgumentParser("Create Board")

    arg_parser.add_argument("-o", "--outdir", required=True,
                            help="The folder where to store the 100 rooms.")
    
    args = arg_parser.parse_args()

    if not exists(args.outdir):
        makedirs(args.outdir)
    
    count_board = 1
    base_edge = 4
    edge_size = base_edge
    multiplier = 0
    divider = 4

    while count_board < 101:
        board = None

        while board is None:
            p_free = 0
            while p_free < 25 or p_wall < 25:
                p_free = choice(range(101))
                p_wall = 100 - p_free

            board = create_board(edge_size, p_free, p_wall)
            if board is not None:
                print(count_board, 
                    f"- Generated board {edge_size}x{edge_size} with {p_free}% "
                    f"free cells and {p_wall}% walls")
        
        with open(args.outdir + sep + str(count_board) + ".json", "w", encoding="utf-8") as f:
            dump(board, f)
        
        multiplier += 1
        edge_size = base_edge * ((multiplier % divider) + 1)
        count_board += 1
