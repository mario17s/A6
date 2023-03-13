#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import copy
import math

def create_complex_number(real_part, imaginary_part):
    return {"real": real_part, "imaginary":imaginary_part}

def get_real_part(complex_number):
    return complex_number["real"]

def set_real_part(complex_number, new_real_part):
    complex_number["real"] = new_real_part

def get_imaginary_part(complex_number):
    return complex_number["imaginary"]

def set_imaginary_part(complex_number, new_imaginary_part):
    complex_number["imaginary"] = new_imaginary_part

def turn_to_string(complex_number):
    if get_imaginary_part(complex_number) < 0:
        return str(get_real_part(complex_number)) + str(get_imaginary_part(complex_number)) + "i"
    return str(get_real_part(complex_number)) + "+" + str(get_imaginary_part(complex_number)) + "i"

def modulo_of_complex_number(complex_number):
    return float(math.sqrt(get_real_part(complex_number) * get_real_part(complex_number) + get_imaginary_part(complex_number) * get_imaginary_part(complex_number)))

def add_complex_number(list_of_complex_numbers, history,  real_part, imaginary_part):
    new_number = create_complex_number(real_part, imaginary_part)
    list_of_complex_numbers.append(new_number)
    history.append(copy.deepcopy(list_of_complex_numbers))

def test_add_complex_number():
    lst = []
    hst = []
    add_complex_number(lst, hst, 4, 5)
    assert lst == [{"real": 4, "imaginary":5}]


def insert_number_at_position(list_of_complex_numbers, history,  real_part, imaginary_part, position):
    if position > len(list_of_complex_numbers):
        raise ValueError("no ok")
    new_number = create_complex_number(real_part, imaginary_part)
    list_of_complex_numbers.insert(position, new_number)
    history.append(copy.deepcopy(list_of_complex_numbers))

def remove_from_position(list_of_complex_numbers, history, position):
    if position >= len(list_of_complex_numbers):
        raise ValueError("the position exceeds the length of the array")
    list_of_complex_numbers.pop(position)
    history.append(copy.deepcopy(list_of_complex_numbers))

def remove_start_to_end_position(list_of_complex_numbers, history, start_position, end_position):
    if start_position < 0:
        raise ValueError("position of start cannot be negative")
    if end_position >= len(list_of_complex_numbers):
        raise ValueError("the position exceeds the length of the array")
    for index in range(0, end_position - start_position + 1):
        list_of_complex_numbers.pop(start_position)
    history.append(copy.deepcopy(list_of_complex_numbers))

def replace_number_with_new_number(list_of_complex_numbers, history, old_real_part, old_imaginary_part, new_real_part, new_imaginary_part):
    for complex_number in list_of_complex_numbers:
        if get_real_part(complex_number) == old_real_part and get_imaginary_part(complex_number) == old_imaginary_part:
            set_real_part(complex_number, new_real_part)
            set_imaginary_part(complex_number, new_imaginary_part)
    history.append(copy.deepcopy(list_of_complex_numbers))

def list_real_start_position_to_end_position(list_of_complex_numbers, history, start_position, end_position):
    if start_position < 0:
        raise ValueError("position of start cannot be negative")
    if end_position >= len(list_of_complex_numbers):
        raise ValueError("the position exceeds the length of the array")
    for index in range(start_position, end_position + 1):
        if get_imaginary_part(list_of_complex_numbers[index]) == 0:
            print(turn_to_string(list_of_complex_numbers[index]), end = " ")
            if index != end_position:
                print("", end = " ")
    print()

def list_modulo_less_than_given_number(list_of_complex_numbers, history, given_number):
    if given_number < 0:
        raise ValueError("modulo cannot be negative")
    for complex_number in list_of_complex_numbers:
        if modulo_of_complex_number(complex_number) < given_number:
            print(turn_to_string(complex_number), end = " ")
    print()

def list_modulo_equal_to_given_number(list_of_complex_numbers, history, given_number):
    if given_number < 0:
        raise ValueError("modulo cannot be negative")
    for complex_number in list_of_complex_numbers:
        if modulo_of_complex_number(complex_number) == given_number:
            print(turn_to_string(complex_number), end = " ")
    print()

def list_modulo_greater_than_given_number(list_of_complex_numbers, history, given_number):
    if given_number < 0:
        raise ValueError("modulo cannot be negative")
    for complex_number in list_of_complex_numbers:
        if modulo_of_complex_number(complex_number) > given_number:
            print(turn_to_string(complex_number), end = " ")
    print()

def filter_real(list_of_complex_numbers, history):
    new_list = []
    for complex_number in list_of_complex_numbers:
        if get_imaginary_part(complex_number) == 0:
            new_list.append(complex_number)
    list_of_complex_numbers.clear()
    list_of_complex_numbers.extend(new_list)
    history.append(copy.deepcopy(list_of_complex_numbers))

def filter_modulo_less_than_given_number(list_of_complex_numbers, history, given_number):
    if given_number < 0:
        raise ValueError("modulo cannot be negative")
    new_list = []
    for complex_number in list_of_complex_numbers:
        print(modulo_of_complex_number(complex_number))
        if modulo_of_complex_number(complex_number) < given_number:
            new_list.append(complex_number)
    list_of_complex_numbers.clear()
    list_of_complex_numbers.extend(new_list)
    history.append(copy.deepcopy(list_of_complex_numbers))

def filter_modulo_equal_to_given_number(list_of_complex_numbers, history, given_number):
    if given_number < 0:
        raise ValueError("modulo cannot be negative")
    new_list = []
    for complex_number in list_of_complex_numbers:
        if modulo_of_complex_number(complex_number) == given_number:
            new_list.append(complex_number)
    list_of_complex_numbers.clear()
    list_of_complex_numbers.extend(new_list)
    history.append(copy.deepcopy(list_of_complex_numbers))

def filter_modulo_greater_than_given_number(list_of_complex_numbers, history, given_number):
    if given_number < 0:
        raise ValueError("modulo cannot be negative")
    new_list = []
    for complex_number in list_of_complex_numbers:
        print(modulo_of_complex_number(complex_number))
        if modulo_of_complex_number(complex_number) > given_number:
            new_list.append(complex_number)
    list_of_complex_numbers.clear()
    list_of_complex_numbers.extend(new_list)
    history.append(copy.deepcopy(list_of_complex_numbers))

test_add_complex_number()