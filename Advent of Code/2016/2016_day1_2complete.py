Nico Baier
nico021218
AdventOfCode

SirPatschiii
 hat den Kanalnamen zu:
AdventOfCode
 geändert.
 — 09.01.2024 19:37
SirPatschiii — 09.01.2024 19:46
def read_input(input_string):
    elements: list = input_string.split(", ")
    calc_dist(elements)


def calc_dist(elements):
    sight = "N"
    x = 0
    y = 0
    koordinates: list[[int, int]] = []

    for elements in elements:
        direction = str(elements[0])
        distance = int(elements[1:])

        if sight == "N":
            if direction == "R":
                x = x + distance
                sight = "O"
                koordinates.append([x, y])
                continue
            if direction == "L":
                x = x - distance
                sight = "W"
                koordinates.append([x, y])
                continue

        if sight == "O":
            if direction == "R":
                y = y - distance
                sight = "S"
                koordinates.append([x, y])
                continue
            if direction == "L":
                y = y + distance
                sight = "N"
                koordinates.append([x, y])
                continue

        if sight == "S":
            if direction == "R":
                x = x - distance
                sight = "W"
                koordinates.append([x, y])
                continue
            if direction == "L":
                x = x + distance
                sight = "O"
                koordinates.append([x, y])
                continue

        if sight == "W":
            if direction == "R":
                y = y + distance
                sight = "N"
                koordinates.append([x, y])
                continue
            if direction == "L":
                y = y - distance
                sight = "S"
                koordinates.append([x, y])
                continue

    calc_blocks(x, y)
    find_first_double(koordinates)


def calc_blocks(x, y):
    x = abs(x)
    y = abs(y)

    print("Die Distanz beträgt: ", end="")
    print(x + y)


def calc_every_intersection(koordinates):
    every_intersection: list[[int, int]] = [[0, 0]]
    x_sum = 0
    y_sum = 0
    c = 0

    for item in koordinates:
        a = item[0]
        b = item[1]
        x = a - x_sum
        y = b - y_sum

        if x < 0:
            for i in range(1, abs(x) + 1):
                every_intersection.append([x_sum - i, y_sum])
                c += 1
            x_sum = x_sum + x
        elif x > 0:
            for i in range(1, abs(x) + 1):
                every_intersection.append([x_sum + i, y_sum])
                c += 1
            x_sum = x_sum + x

        if y < 0:
            for j in range(1, abs(y) + 1):
... (52 Zeilen verbleibend)
Einklappen
AdventOfCode2016A1Complete.py
5 kB
Zur Vollständigkeit hier noch die komplette Aufgabe 1
Vives — 09.01.2024 19:58

def codezifferUD(chr, positionUD):
    if chr == "D":
        if positionUD>=0 and positionUD<2:
            positionUD +=1
        return positionUD

    elif chr == "U":
        if positionUD>0 and positionUD<=2:
            positionUD -=1
        return positionUD
    return positionUD

def codezifferLR(chr, positionLR):
    if chr == "R":
        if positionLR >= 0 and positionLR < 2:
            positionLR += 1
        return positionLR

    elif chr == "L":
        if positionLR > 0 and positionLR <= 2:
            positionLR -= 1
        return positionLR
    return positionLR


with open("C:\\Users\\Admin\\Documents\\AOC\\2016Day2.1.txt") as file:
    input = file.readlines()
codefeld = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
indexUD = 1
indexLR = 1
x: list[int] = []
for zeile in input:
    arr = list(zeile)
    for anweisung in arr:
        indexUD = codezifferUD(anweisung, indexUD)
        indexLR = codezifferLR(anweisung, indexLR)
    x.append(codefeld[indexUD][indexLR])
for a in x:
    print(a)
Einklappen
2016Day2.1.py
2 kB
Hat geklappt
Nico Baier — 09.01.2024 22:06
👍
﻿
def read_input(input_string):
    elements: list = input_string.split(", ")
    calc_dist(elements)


def calc_dist(elements):
    sight = "N"
    x = 0
    y = 0
    koordinates: list[[int, int]] = []

    for elements in elements:
        direction = str(elements[0])
        distance = int(elements[1:])

        if sight == "N":
            if direction == "R":
                x = x + distance
                sight = "O"
                koordinates.append([x, y])
                continue
            if direction == "L":
                x = x - distance
                sight = "W"
                koordinates.append([x, y])
                continue

        if sight == "O":
            if direction == "R":
                y = y - distance
                sight = "S"
                koordinates.append([x, y])
                continue
            if direction == "L":
                y = y + distance
                sight = "N"
                koordinates.append([x, y])
                continue

        if sight == "S":
            if direction == "R":
                x = x - distance
                sight = "W"
                koordinates.append([x, y])
                continue
            if direction == "L":
                x = x + distance
                sight = "O"
                koordinates.append([x, y])
                continue

        if sight == "W":
            if direction == "R":
                y = y + distance
                sight = "N"
                koordinates.append([x, y])
                continue
            if direction == "L":
                y = y - distance
                sight = "S"
                koordinates.append([x, y])
                continue

    calc_blocks(x, y)
    find_first_double(koordinates)


def calc_blocks(x, y):
    x = abs(x)
    y = abs(y)

    print("Die Distanz beträgt: ", end="")
    print(x + y)


def calc_every_intersection(koordinates):
    every_intersection: list[[int, int]] = [[0, 0]]
    x_sum = 0
    y_sum = 0
    c = 0

    for item in koordinates:
        a = item[0]
        b = item[1]
        x = a - x_sum
        y = b - y_sum

        if x < 0:
            for i in range(1, abs(x) + 1):
                every_intersection.append([x_sum - i, y_sum])
                c += 1
            x_sum = x_sum + x
        elif x > 0:
            for i in range(1, abs(x) + 1):
                every_intersection.append([x_sum + i, y_sum])
                c += 1
            x_sum = x_sum + x

        if y < 0:
            for j in range(1, abs(y) + 1):
                every_intersection.append([x_sum, y_sum - j])
                c += 1
            y_sum = y_sum + y
        elif y > 0:
            for j in range(1, abs(y) + 1):
                every_intersection.append([x_sum, y_sum + j])
                c += 1
            y_sum = y_sum + y

    return every_intersection


def find_first_double(koordinates):
    every_intersection = calc_every_intersection(koordinates)
    doubles: list[[int, int]] = []
    ranges: list[int] = []
    start = -1
    for element in every_intersection:
        c = 0
        start += 1
        for i in range(start, len(every_intersection)):
            if every_intersection[i] == element:
                c += 1
            if c >= 2:
                doubles.append(element)
                ranges.append(i)
                break

    for i in range(len(ranges)):
        temp_r = ranges[i]
        temp_d = doubles[i]
        j = i - 1
        while j >= 0 and ranges[j] > temp_r:
            ranges[j + 1] = ranges[j]
            doubles[j + 1] = doubles[j]
            j = j - 1
        ranges[j + 1] = temp_r
        doubles[j + 1] = temp_d


    for element in doubles:
        distance = abs(element[0]) + abs(element[1])
        print("Die Distanz zur ersten Kreuzung die doppelt vorkommt beträgt: " + str(distance))
        break

def main():
    read_input(str(input("Wie ist die Zeichenfolge? \n")))


if __name__ == "__main__":
    main()