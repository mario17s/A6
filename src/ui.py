#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import copy

from src.functions import add_complex_number, turn_to_string, insert_number_at_position, remove_from_position, \
    remove_start_to_end_position, replace_number_with_new_number, get_imaginary_part, \
    list_real_start_position_to_end_position, list_modulo_less_than_given_number, list_modulo_equal_to_given_number, \
    list_modulo_greater_than_given_number, filter_real, filter_modulo_less_than_given_number, \
    filter_modulo_equal_to_given_number, filter_modulo_greater_than_given_number


def get_parameters_for_complex_number(string_complex_number):
    position_of_plus = string_complex_number.find('+')
    position_of_minus = string_complex_number.find('-')
    if position_of_plus != -1 and position_of_minus == -1:
        string_complex_number = string_complex_number.split("+")
        string_complex_number = [element.strip("i") for element in string_complex_number]
        return string_complex_number
    elif position_of_plus == -1 and position_of_minus != -1:
        string_complex_number = string_complex_number[:position_of_minus] + " " + string_complex_number[position_of_minus:]
        string_complex_number = string_complex_number.split(" ")
        string_complex_number = [element.strip("i") for element in string_complex_number]
        return string_complex_number
    elif position_of_plus != -1 and position_of_minus != -1 and position_of_minus < position_of_plus:
        string_complex_number = string_complex_number.split("+")
        string_complex_number = [element.strip("i") for element in string_complex_number]
        return string_complex_number
    else:
        if "i" in string_complex_number:
            string_complex_number = string_complex_number.strip("i")
            return ['0', string_complex_number]
        else:
            return [string_complex_number, '0']
def read_command():
    command = input(">")
    position = command.find(" ")
    if position == -1:
        return command, []
    command_given = command[:position]
    if command_given == "list":
        arguments_given = command[position + 1:]
        if "real" in arguments_given and "to" in arguments_given:
            command_given = "list real start position to end position"
            arguments_given = arguments_given.split(" ")
            arguments_given.remove("real")
            arguments_given.remove("to")
        if "modulo" in arguments_given:
            arguments_given = arguments_given.split(" ")
            arguments_given.remove("modulo")
            if "<" in arguments_given:
                command_given = "list modulo less than number"
                arguments_given.remove("<")
            if "=" in arguments_given:
                command_given = "list modulo equal to number"
                arguments_given.remove("=")
            if ">" in arguments_given:
                command_given = "list modulo greater than number"
                arguments_given.remove(">")
    if command_given == "add":
        arguments_given = command[position + 1:]
        arguments_given = get_parameters_for_complex_number(arguments_given)
    if command_given == "insert":
        arguments = command[position + 1:]
        if "at" in arguments:
            command_given = "insert at"
            arguments = arguments.split(" ")
            arguments.remove("at")
            arguments_given = get_parameters_for_complex_number(arguments[0])
            arguments_given.append(arguments[1])
    if command_given == "remove":
        arguments_given = command[position + 1:]
        if "to" not in arguments_given:
            command_given = "remove from position"
        else:
            command_given = "remove start position to end position"
            arguments_given = arguments_given.split(" ")
            arguments_given.remove("to")
    if command_given == "replace":
        command_given = "replace number with new number"
        arguments = command[position + 1:]
        arguments = arguments.split(" ")
        arguments.remove("with")
        arguments_given = get_parameters_for_complex_number(arguments[0])
        arguments_given.extend(get_parameters_for_complex_number(arguments[1]))
    if command_given == "filter":
        arguments_given = command[position + 1:]
        if "real" in arguments_given:
            command_given = "filter real"
            arguments_given = []
        if "modulo" in arguments_given:
            arguments_given = arguments_given.split(" ")
            arguments_given.remove("modulo")
            if "<" in arguments_given:
                command_given = "filter modulo less than number"
                arguments_given.remove("<")
            if "=" in arguments_given:
                command_given = "filter modulo equal to number"
                arguments_given.remove("=")
            if ">" in arguments_given:
                command_given = "filter modulo greater than number"
                arguments_given.remove(">")
    return command_given, arguments_given

def print_options(commands):
    print(*list(commands.keys()), sep = "\n")

def print_list_of_complex_numbers(list_of_complex_numbers, history):
    for complex_number in list_of_complex_numbers:
        print(turn_to_string(complex_number), end = " ")
    print()

def add_complex_number_ui(list_of_complex_numbers, history, real_part = 0, imaginary_part = 0):
    try:
        real_part = int(real_part)
        imaginary_part = int(imaginary_part)
        add_complex_number(list_of_complex_numbers, history, real_part, imaginary_part)
    except ValueError as ve:
        print(ve)

def insert_number_at_position_ui(list_of_complex_numbers, history, real_part = 0, imaginary_part = 0, position = 0):
    try:
        real_part = int(real_part)
        imaginary_part = int(imaginary_part)
        position = int(position)
        insert_number_at_position(list_of_complex_numbers, history, real_part, imaginary_part, position)
    except ValueError as ve:
        print(ve)

def remove_from_position_ui(list_of_complex_numbers, history, position):
    try:
        position = int(position)
        remove_from_position(list_of_complex_numbers, history, position)
    except ValueError as ve:
        print(ve)

def remove_start_to_end_position_ui(list_of_complex_numbers, history, start_position, end_position):
    try:
        start_position = int(start_position)
        end_position = int(end_position)
        remove_start_to_end_position(list_of_complex_numbers, history, start_position, end_position)
    except ValueError as ve:
        print(ve)

def replace_number_with_new_number_ui(list_of_complex_numbers, history, old_real_part, old_imaginary_part, new_real_part, new_imaginary_part):
    try:
        old_real_part = int(old_real_part)
        old_imaginary_part = int(old_imaginary_part)
        new_real_part = int(new_real_part)
        new_imaginary_part = int(new_imaginary_part)
        replace_number_with_new_number(list_of_complex_numbers, history, old_real_part, old_imaginary_part, new_real_part, new_imaginary_part)
    except ValueError as ve:
        print(ve)

def list_real_start_position_to_end_position_ui(list_of_complex_numbers, history, start_position, end_position):
    try:
        start_position = int(start_position)
        end_position = int(end_position)
        list_real_start_position_to_end_position(list_of_complex_numbers, history, start_position, end_position)
    except ValueError as ve:
        print(ve)


def list_modulo_less_than_given_number_ui(list_of_complex_numbers, history, given_number):
    try:
        given_number = int(given_number)
        list_modulo_less_than_given_number(list_of_complex_numbers, history, given_number)
    except ValueError as ve:
        print(ve)

def list_modulo_equal_to_given_number_ui(list_of_complex_numbers, history, given_number):
    try:
        given_number = int(given_number)
        list_modulo_equal_to_given_number(list_of_complex_numbers, history, given_number)
    except ValueError as ve:
        print(ve)

def list_modulo_greater_than_given_number_ui(list_of_complex_numbers, history, given_number):
    try:
        given_number = int(given_number)
        list_modulo_greater_than_given_number(list_of_complex_numbers, history, given_number)
    except ValueError as ve:
        print(ve)

def filter_real_ui(list_of_complex_numbers, history):
    try:
        filter_real(list_of_complex_numbers, history)
    except ValueError as ve:
        print(ve)

def filter_modulo_less_than_given_number_ui(list_of_complex_numbers, history, given_number):
    try:
        given_number = int(given_number)
        filter_modulo_less_than_given_number(list_of_complex_numbers, history, given_number)
    except ValueError as ve:
        print(ve)

def filter_modulo_equal_to_given_number_ui(list_of_complex_numbers, history, given_number):
    try:
        given_number = int(given_number)
        filter_modulo_equal_to_given_number(list_of_complex_numbers, history, given_number)
    except ValueError as ve:
        print(ve)

def filter_modulo_greater_than_given_number_ui(list_of_complex_numbers, history, given_number):
    try:
        given_number = int(given_number)
        filter_modulo_greater_than_given_number(list_of_complex_numbers, history, given_number)
    except ValueError as ve:
        print(ve)

def undo_operation(list_of_complex_numbers, history):
    history.pop()
    list_of_complex_numbers.clear()
    list_of_complex_numbers.extend(history[-1])

def run_console():
    list_of_complex_numbers = [{"real" : 3, "imaginary" : 4}, {"real" : 2, "imaginary" : 3}, {"real" : 3, "imaginary" : 0},
    {"real" : 4, "imaginary" : 5}, {"real" : 5, "imaginary" : 0}, {"real" : 6, "imaginary" : 0}]
    history = []
    history.append(copy.deepcopy(list_of_complex_numbers))
    commands = {
        "add" : add_complex_number_ui,
        "list" : print_list_of_complex_numbers,
        "undo" : undo_operation,
        "insert at": insert_number_at_position_ui,
        "remove from position": remove_from_position_ui,
        "remove start position to end position": remove_start_to_end_position_ui,
        "replace number with new number": replace_number_with_new_number_ui,
        "list real start position to end position": list_real_start_position_to_end_position_ui,
        "list modulo less than number": list_modulo_less_than_given_number_ui,
        "list modulo equal to number": list_modulo_equal_to_given_number_ui,
        "list modulo greater than number": list_modulo_greater_than_given_number_ui,
        "filter real": filter_real_ui,
        "filter modulo less than number": filter_modulo_less_than_given_number_ui,
        "filter modulo equal to number": filter_modulo_equal_to_given_number_ui,
        "filter modulo greater than number": filter_modulo_greater_than_given_number_ui
    }
    while True:
        print_options(commands)
        command, arguments = read_command()
        if command == "exit":
            break
        try:
            commands[command](list_of_complex_numbers, history, *arguments)
        except KeyError as ke:
            print("this option is not valid", ke)
