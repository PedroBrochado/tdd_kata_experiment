
def add(number_string):
    string_list = number_string.split(",")
    int_list = [int(element) for element in string_list if element != ""]
    return sum(int_list)
