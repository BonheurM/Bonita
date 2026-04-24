"""
Step 1 of the custom language interpreter.

For now, this program only:
1. Opens a text file
2. Reads it line by line
3. Prints each line

This gives us a simple starting point before we add variables and commands.
"""

import sys


def run_file(filename):
    """Read the program file line by line and print each line."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                # Remove the newline at the end so output is cleaner.
                print(f"Line {line_number}: {line.strip()}")
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
