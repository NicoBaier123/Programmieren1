def checkzero(positionLR,positionUD,chr):

    if chr=="U":
        if positionUD > 0 and positionUD <= 4:
            if codefeld[positionUD-1][positionLR]=="0":
                return True

    if chr == "D":
        if positionUD >= 0 and positionUD < 4:
            if codefeld[positionUD + 1][positionLR] == "0":
                return True

    if chr == "L":
        if positionLR > 0 and positionLR <= 4:
            if codefeld[positionUD][positionLR-1] == "0":
                return True

    if chr == "R":
        if positionLR >= 0 and positionLR < 4:
            if codefeld[positionUD][positionLR+1] == "0":
                return True
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


with open("D:\\Schule\\Programmieren\\Programmieren1\\Advent of Code\\2016\\aoc-2016-day2.txt") as file:
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

