
def add(number_string):
    string_list = number_string.split(",")
    string_list = [x.split("\n") for x in string_list]

    return sum(sum_list_of_strings(x) for x in string_list)


def sum_list_of_strings(string_list):
    int_list = [int(element) for element in string_list if element != ""]
    return sum(int_list)



