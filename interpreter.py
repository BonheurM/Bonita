"""
Simple interpreted language for a Programming Languages final project.

Language features:
- variables stored in a dictionary
- integers and strings
- user input
- printing output
- arithmetic
- conditionals
- loops

Core keywords/operators:
- PRINT value
- INPUT var
- SET var value
- ADD x y result
- SUB x y result
- MUL x y result
- MOD x y result
- LEN text result
- CHAR text index result
- CONCAT x y result
- IF x operator y
- WHILE x operator y
- END

Each line in the program file is one command.
The interpreter splits the line into tokens and uses the first token
to decide what to do.
"""

import sys


def get_value(token, variables):
    """
    Convert one token into its real value.

    Rules:
    - variable name -> variable value
    - "quoted text" -> string
    - integer text -> int
    - anything else -> plain string
    """
    if token in variables:
        return variables[token]

    if len(token) >= 2 and token[0] == '"' and token[-1] == '"':
        return token[1:-1]

    if token.lstrip("-").isdigit():
        return int(token)

    return token


def load_program(filename):
    """Read the file and return a cleaned list of program lines."""
    lines = []

    with open(filename, "r", encoding="utf-8") as file:
        for raw_line in file:
            clean_line = raw_line.strip()

            # Skip blank lines and comment lines.
            if clean_line == "" or clean_line.startswith("#"):
                continue

            lines.append(clean_line)

    return lines


def evaluate_condition(tokens, variables):
    """Evaluate a simple condition such as x == y or count > 0."""
    if len(tokens) != 3:
        print("Error: Condition must look like x operator y.")
        return False

    left = get_value(tokens[0], variables)
    operator = tokens[1]
    right = get_value(tokens[2], variables)

    if operator == "==":
        return left == right
    if operator == "!=":
        return left != right
    if operator == "<":
        return left < right
    if operator == ">":
        return left > right
    if operator == "<=":
        return left <= right
    if operator == ">=":
        return left >= right

    print(f"Error: Unknown operator '{operator}'.")
    return False


def find_matching_end(lines, start_index):
    """
    Find the END that matches an IF or WHILE.

    This also works for nested blocks.
    """
    depth = 0

    for index in range(start_index, len(lines)):
        tokens = lines[index].split()

        if not tokens:
            continue

        command = tokens[0]

        if command in ("IF", "WHILE"):
            depth += 1
        elif command == "END":
            depth -= 1

            if depth == 0:
                return index

    return -1


def run_math_command(command, tokens, variables):
    """Run ADD, SUB, MUL, or MOD."""
    if len(tokens) != 4:
        print(f"Error: {command} needs x y result.")
        return

    x = get_value(tokens[1], variables)
    y = get_value(tokens[2], variables)
    result_name = tokens[3]

    if not isinstance(x, int) or not isinstance(y, int):
        print(f"Error: {command} only works with integers.")
        return

    if command == "ADD":
        variables[result_name] = x + y
    elif command == "SUB":
        variables[result_name] = x - y
    elif command == "MUL":
        variables[result_name] = x * y
    elif command == "MOD":
        if y == 0:
            print("Error: Cannot divide by zero in MOD.")
            return
        variables[result_name] = x % y


def execute_simple_command(line, variables):
    """Execute commands that do not create blocks."""
    tokens = line.split()

    if not tokens:
        return

    command = tokens[0]

    if command == "PRINT":
        if len(tokens) < 2:
            print("Error: PRINT needs a value.")
            return

        value_text = " ".join(tokens[1:])
        print(get_value(value_text, variables))

    elif command == "SET":
        if len(tokens) < 3:
            print("Error: SET needs a variable and a value.")
            return

        var_name = tokens[1]
        value_text = " ".join(tokens[2:])
        variables[var_name] = get_value(value_text, variables)

    elif command == "INPUT":
        if len(tokens) != 2:
            print("Error: INPUT needs one variable name.")
            return

        user_text = input()

        if user_text.lstrip("-").isdigit():
            variables[tokens[1]] = int(user_text)
        else:
            variables[tokens[1]] = user_text

    elif command in ("ADD", "SUB", "MUL", "MOD"):
        run_math_command(command, tokens, variables)

    elif command == "LEN":
        if len(tokens) != 3:
            print("Error: LEN needs text result.")
            return

        # Convert values to text so inputs like 4 can be processed as strings.
        text = str(get_value(tokens[1], variables))
        result_name = tokens[2]

        variables[result_name] = len(text)

    elif command == "CHAR":
        if len(tokens) != 4:
            print("Error: CHAR needs text index result.")
            return

        # Convert values to text so numeric input can still be used as text.
        text = str(get_value(tokens[1], variables))
        index = get_value(tokens[2], variables)
        result_name = tokens[3]

        if not isinstance(index, int):
            print("Error: CHAR index must be an integer.")
            return

        if 0 <= index < len(text):
            variables[result_name] = text[index]
        else:
            print("Error: CHAR index is out of range.")

    elif command == "CONCAT":
        if len(tokens) != 4:
            print("Error: CONCAT needs x y result.")
            return

        first = get_value(tokens[1], variables)
        second = get_value(tokens[2], variables)
        result_name = tokens[3]
        variables[result_name] = str(first) + str(second)

    else:
        print(f"Error: Unknown command '{command}'.")


def execute_block(lines, variables, start_index=0, end_index=None):
    """Execute a block of lines from start_index up to end_index."""
    if end_index is None:
        end_index = len(lines)

    index = start_index

    while index < end_index:
        line = lines[index]
        tokens = line.split()

        if not tokens:
            index += 1
            continue

        command = tokens[0]

        if command == "IF":
            block_end = find_matching_end(lines, index)

            if block_end == -1:
                print("Error: IF is missing END.")
                return

            if evaluate_condition(tokens[1:], variables):
                execute_block(lines, variables, index + 1, block_end)

            index = block_end + 1

        elif command == "WHILE":
            block_end = find_matching_end(lines, index)

            if block_end == -1:
                print("Error: WHILE is missing END.")
                return

            while evaluate_condition(tokens[1:], variables):
                execute_block(lines, variables, index + 1, block_end)

            index = block_end + 1

        elif command == "END":
            return

        else:
            execute_simple_command(line, variables)
            index += 1


def run_file(filename):
    """Load the program file and run it."""
    try:
        variables = {}
        program_lines = load_program(filename)
        execute_block(program_lines, variables)
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'.")
    except Exception as error:
        print(f"Error: {error}")


def main():
    """Get the filename from the command line and run the file."""
    if len(sys.argv) < 2:
        print("Usage: python3 interpreter.py program.txt")
        return

    run_file(sys.argv[1])


if __name__ == "__main__":
    main()
