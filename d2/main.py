import argparse
import numpy as np
import re

parser = argparse.ArgumentParser()
parser.add_argument('input')

args = parser.parse_args()

def part1(lines, test):
    pgames = []
    for line in lines:
        m = re.match("^Game (\d+): (.*)$", line)
        game_num = m.group(1)
        post = m.group(2)
        sets = post.split("; ")
        poss = True
        for s in sets:
            cubes = s.split(", ")
            for cube in cubes:
                ss = cube.split(" ")
                num = int(ss[0])
                color = ss[1]
                if test[color] < num:
                    poss = False
                    break
            if not poss:
                break
        if poss:
            pgames.append(int(game_num))
    return np.sum(pgames)

def part2(lines):
    pgames = []
    for line in lines:
        max_of_cubes = {}
        m = re.match("^Game (\d+): (.*)$", line)
        game_num = m.group(1)
        post = m.group(2)
        sets = post.split("; ")
        for s in sets:
            cubes = s.split(", ")
            for cube in cubes:
                ss = cube.split(" ")
                num = int(ss[0])
                color = ss[1]
                if color in max_of_cubes:
                    max_of_cubes[color] = max(max_of_cubes[color], num)
                else:
                    max_of_cubes[color] = num
        power = 1
        for i, n in max_of_cubes.items():
            power *= n
        pgames.append(power)
    return np.sum(pgames)


with open(args.input, 'r') as f:
    lines = f.readlines()
    test = {"red": 12, "green": 13, "blue": 14}
    print(f"Part one: {part1(lines, test)}")
    print(f"Part two: {part2(lines)}")
