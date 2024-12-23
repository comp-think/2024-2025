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

from json import load
from os.path import exists, sep
from os import remove
from collections import Counter
import john_doe

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"


def load_room(room_file_path):
    with open(room_file_path, encoding="utf-8") as f:
        room_json = load(f)
        
        return room_json["structure"], (room_json["cannon"]["x"], room_json["cannon"]["y"])


def get_direction(start_position, end_position):
    x_axis, y_axis = 0, 0
    x1, y1 = start_position
    x2, y2 = end_position

    if x1 < x2:
        x_axis = +1
    elif x1 > x2:
        x_axis = -1

    if y1 < y2:
        y_axis = +1
    elif y1 > y2:
        y_axis = -1
    
    return x_axis, y_axis


def is_valid_move(cannon, walls_to_remove, walls, limit):
    # At least one wall should be removed
    if len(walls_to_remove) == 0:
        return False, 0

    # The walls to remove must exist
    for wall in walls_to_remove:
        if wall not in walls:
            return False, 0
    
    # Avoid destroying the cannon
    for wall in walls_to_remove:
        if wall == cannon:
            return False, 0
    
    d_x, d_y = get_direction(cannon, walls_to_remove[0])
    c_x, c_y = cannon[0] + d_x, cannon[1] + d_y
    count_walls_to_hit = 0
    count_hit_walls = 0
    
    while c_x > -1 and c_x <= limit and c_y > -1 and c_y <= limit:
        if (c_x, c_y) in walls:
            count_walls_to_hit += 1
            if (c_x, c_y) in walls_to_remove:
                count_hit_walls += 1
            
        c_x += d_x
        c_y += d_y
        
    return True, count_hit_walls


def predict(room, walls, cannon):
    limit = len(room[0])

    diff = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (1, -1), (-1, 1),
        (1, 1), (-1, -1)
    ]

    best_result = 0

    for d_x, d_y in diff:
        walls_hit = 0
        c_x, c_y = cannon[0] + d_x, cannon[1] + d_y

        while c_x > -1 and c_x <= limit and c_y > -1 and c_y <= limit:
            if (c_x, c_y) in walls:
                walls_hit += 1
            
            c_x += d_x
            c_y += d_y
        
        if walls_hit > best_result:
            best_result = walls_hit
    
    return best_result


def get_walls(room):
    walls = set()

    for row in room:
        for cell in row:
            if cell["type"] == "wall":
                walls.add((cell["x"], cell["y"]))
    
    return walls


def play(players, cannon, room):
    cheaters, loosers, winners = set(), set(), set()
    walls = get_walls(room)
    prediction = predict(room, walls, cannon)

    for player in players:
        player_name = player.__name__
        
        try:
            walls_to_remove = player.do_move(room, cannon)
        except:
            walls_to_remove = []

        is_valid, count = is_valid_move(cannon, walls_to_remove, walls, len(room[0]))

        if is_valid:
            if prediction == count:
                winners.add((player_name, 0))
            else:
                loosers.add((player_name, abs(prediction - count)))
        else:
            cheaters.add((player_name, abs(prediction - count)))
    
    return cheaters, loosers, winners

if __name__ == "__main__":
    all_players = [john_doe]

    final_results = {
        "cheaters": {},
        "winners": {},
        "loosers": {},
        "rank": {}
    }

    if exists("00_results.txt"):
        remove("00_results.txt")

    all_players_name = set()
    for player in all_players:
        player_name = player.__name__
        all_players_name.add(player_name)
        final_results["cheaters"][player_name] = 0
        final_results["winners"][player_name] = 0
        final_results["loosers"][player_name] = 0
        final_results["rank"][player_name] = 0

    for idx in range(1, 101):
        print("# Room", idx)

        cur_room, cur_cannon = load_room("rooms" + sep + str(idx) + ".json")
        edge_size = len(cur_room)
        
        cheaters, loosers, winners = play(all_players, cur_cannon, cur_room)

        for player_name, count in cheaters:
            final_results["cheaters"][player_name] += 1
            final_results["rank"][player_name] += count

        for player_name, count in loosers:
            final_results["loosers"][player_name] += 1
            final_results["rank"][player_name] += count
        
        for player_name, count in winners:
            final_results["winners"][player_name] += 1

        winners_string = ", ".join(sorted([player[0] + " (" + str(player[1]) + ")" for player in winners]))
        loosers_string = ", ".join(sorted([player[0] + " (" + str(player[1]) + ")" for player in loosers]))
        cheaters_string = ", ".join(sorted([player[0] + " (" + str(player[1]) + ")" for player in cheaters]))
        
        with open("00_results.txt", "a", encoding="utf-8") as f:
            f.write("\n" + "# Room " + str(idx) + "\n\twinners: "+ winners_string + "\n\tloosers: "+ loosers_string + "\n\tcheaters: "+ cheaters_string + "\n")
    
    # 1. Avoiding cheating (i.e. no walls destroyed or pretending destroying a wall)
    avoid_cheating = all_players_name.difference(set(
        [player_name for player_name in final_results["cheaters"] 
         if final_results["cheaters"][player_name] > 0]))

    # 2. Destroying at least 30 rooms
    destroy_30 = set([player_name for player_name in final_results["winners"] 
                      if final_results["winners"][player_name] > 29])

    # 3. Destroying at least 90 rooms
    destroy_90 = set([player_name for player_name in final_results["winners"] 
                      if final_results["winners"][player_name] > 89])
    
    # 4. Best rank (e.g. minimum number of walls missed)
    best_rank = {k: v for k, v in Counter(final_results["rank"]).items() if v == min(Counter(final_results["rank"]).values())}

    final_results_str = "\n\n## FINAL RESULTS ##\nAvoiding cheating (i.e. no walls destroyed or pretending destroying a wall): " +  " ".join(avoid_cheating) + "\nWinning at least 30 mazes: " + " ".join(destroy_30) + "\nWinning at least 90 mazes: " + " ".join(destroy_90) + "\nBest rank (e.g. minimum number of walls missed): " + " ".join(best_rank)

    with open("00_results.txt", "a", encoding="utf-8") as f:
        f.write(final_results_str)
    
    print(final_results_str)
