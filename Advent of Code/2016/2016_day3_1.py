def get_numbers(str_element):
    v_output_list = [None for _ in range(3)]
    c = 2
    str_element = str(str_element)

    v_list = str_element.split(" ")

    for i in range(len(v_list) - 1, 0, -1):
        if v_list[i] == "":
            continue
        v_output_list[c] = int(v_list[i])
        c -= 1

    return v_output_list


def calc_valid_triangles(input_list):
    c = 0
    for line in input_list:
        v_list = get_numbers(line)
        if (v_list[0] + v_list[1]) > v_list[2] and (v_list[0] + v_list[2]) > v_list[1] and (v_list[1] + v_list[2]) > v_list[0]:
            c += 1

    return c


def file_input():
    with open("C:\\Users\\Nico\\Desktop\\Schule\\Programmieren\\Vs code\\Programmieren1\Advent of Code\\2016\\Tag3.txt") as file:
        v_list = file.readlines()

    return v_list


def main():
    v_sum = calc_valid_triangles(file_input())

    print(f"The sum of valid triangles is {v_sum}.")


if __name__ == '__main__':
    main()