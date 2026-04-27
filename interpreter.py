"""
Step 3 of the custom language interpreter.

This version supports:
- variables stored in a dictionary
- PRINT
- SET
- INPUT
- ADD
- SUB
- MUL

The interpreter reads one line at a time, splits the line into tokens,
and decides what to do based on the first word.
"""

import sys


def get_value(token, variables):
    """
    Return the real value for a token.

    Rules:
    - If the token is a variable name, return the variable's value
    - If the token is an integer, return it as an int
    - Otherwise, return it as a string
    """
    if token in variables:
        return variables[token]

    if token.lstrip("-").isdigit():
        return int(token)

    return token


def execute_line(line, variables):
    """Execute one line of the custom language."""
    tokens = line.split()

    if not tokens:
        return

    command = tokens[0]

    if command == "PRINT":
        if len(tokens) < 2:
            print("Error: PRINT needs a value.")
            return

        value_text = " ".join(tokens[1:])
        value = get_value(value_text, variables)
        print(value)

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

        var_name = tokens[1]
        user_text = input()

        if user_text.lstrip("-").isdigit():
            variables[var_name] = int(user_text)
        else:
            variables[var_name] = user_text

    elif command == "ADD":
        if len(tokens) != 4:
            print("Error: ADD needs x y result.")
            return

        x = get_value(tokens[1], variables)
        y = get_value(tokens[2], variables)
        result_name = tokens[3]

        if isinstance(x, int) and isinstance(y, int):
            variables[result_name] = x + y
        else:
            print("Error: ADD only works with integers.")

    elif command == "SUB":
        if len(tokens) != 4:
            print("Error: SUB needs x y result.")
            return

        x = get_value(tokens[1], variables)
        y = get_value(tokens[2], variables)
        result_name = tokens[3]

        if isinstance(x, int) and isinstance(y, int):
            variables[result_name] = x - y
        else:
            print("Error: SUB only works with integers.")

    elif command == "MUL":
        if len(tokens) != 4:
            print("Error: MUL needs x y result.")
            return

        x = get_value(tokens[1], variables)
        y = get_value(tokens[2], variables)
        result_name = tokens[3]

        if isinstance(x, int) and isinstance(y, int):
            variables[result_name] = x * y
        else:
            print("Error: MUL only works with integers.")

    else:
        print(f"Error: Unknown command '{command}'.")


def run_file(filename):
    """Read the program file line by line and execute each command."""
    try:
        # This dictionary stores the program's variables.
        variables = {}

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()

                # Skip blank lines so they do not cause errors.
                if clean_line == "":
                    continue

                execute_line(clean_line, variables)
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'.")
    except Exception as error:
        print(f"Error: {error}")


def main():
    """Get the filename from the command line and run the file."""
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py program.txt")
        return

    filename = sys.argv[1]
    run_file(filename)


if __name__ == "__main__":
    main()
