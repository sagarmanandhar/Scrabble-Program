import builtins

input_values_1 = []
print_values_1 = []


def mock_input_1(s):
    print_values_1.append(s)
    return input_values_1.pop()


def mock_input_output_start_1():
    global input_values_1, print_values_1

    input_values_1 = []
    print_values_1 = []

    builtins.input = mock_input_1
    builtins.print = lambda s: print_values_1.append(s)


def get_display_output():
    global print_values_1
    return print_values_1


def set_keyboard_input(mocked_inputs_1):
    global input_values_1

    mock_input_output_start_1()
    input_values_1 = mocked_inputs_1