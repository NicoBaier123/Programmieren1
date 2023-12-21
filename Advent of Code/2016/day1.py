import math


def read_input(input_string):
    elements: list = input_string.split(", ")
    calc_dist(elements)


def calc_dist(elements):
    sight = "N"
    x = 0
    y = 0
    counter = True



    for elements in elements:
        direction = str(elements[0])
        distance = int(elements[1:])
        if counter:
            if direction == "L":
                sight = "W"
                counter = False
            else:
                sight = "O"
                counter = False

        if sight == "N":
            if direction == "R":
                x = x + distance
                sight = "O"
                continue
            if direction == "L":
                x = x - distance
                sight = "W"
                continue
        if sight == "O":
            if direction == "R":
                y = y - distance
                sight = "S"
                continue
            if direction == "L":
                y = y + distance
                sight = "N"
                continue

        if sight == "S":
            if direction == "R":
                x = x - distance
                sight = "W"
                continue
            if direction == "L":
                x = x + distance
                sight = "O"
                continue

        if sight == "W":
            if direction == "R":
                y = y + distance
                sight = "N"
                continue
            if direction == "L":
                y = y - distance
                sight = "S"
                continue
    calc_blocks(x, y)

def calc_blocks(x, y):
    x = abs(x)
    y = abs(y)

    print(x + y)
    pass


def main():
    read_input(str(input("Wie ist die Zeichenfolge? \n")))


if __name__ == "__main__":
    main()
