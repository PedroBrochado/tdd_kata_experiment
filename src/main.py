
def add(input_string):
    string_list = input_to_string_list(input_string)

    return sum(sum_list_of_strings(x) for x in string_list)


def input_to_string_list(input_string):
    lines = input_string.split("\n")
    if lines[0].startswith("//"):
        delimiter = lines[0][-1]
        data = lines[1:]
    else:
        delimiter = ","
        data = lines
    return [x.split(delimiter) for x in data]


def sum_list_of_strings(string_list):
    int_list = [int(element) for element in string_list if element != ""]
    return sum(int_list)



