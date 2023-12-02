import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input')

args = parser.parse_args()

def part1(lines):
    vals = []
    for line in lines:
        first = None
        last = None
        for i in range(len(line)):
            inv = len(line) - 1 - i
            if first == None:
                if line[i].isnumeric():
                    first = int(line[i])
            if last == None:
                if line[inv].isnumeric():
                    last = int(line[inv])
            if first != None and last != None:
                break
        vals.append(first * 10 + last)
    return np.sum(vals)

def part2(lines):
    vals = []
    for line in lines:
        first = None
        last = None
        for i in range(len(line)):
            inv = len(line) - 1 - i
            if first == None:
                if line[i].isnumeric():
                    first = int(line[i])
                for j in range(len(spell)):
                    if line[i:].startswith(spell[j]):
                        first = j + 1
            if last == None:
                if line[inv].isnumeric():
                    last = int(line[inv])
                for j in range(len(spell)):
                    if line[:inv+1].endswith(spell[j]):
                        last = j + 1
            if first != None and last != None:
                break
        vals.append(first * 10 + last)
    return np.sum(vals)


with open(args.input, 'r') as f:
    lines = f.readlines()
    spell = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    print(f"Part one: {part1(lines)}")
    print(f"Part two: {part2(lines)}")
