# Bonita Programming Language

This project is a very simple interpreted language written in Python.
The goal of the project is to design a small custom language and build
an interpreter that reads a `.txt` program file and executes one command
per line.

The interpreter is intentionally simple and readable. It does not use
advanced parsing libraries. Instead, it reads the program line by line,
splits each line into tokens, and decides what to do based on the first
word of the line.

## Language Features

The language supports:

- variables
- integers
- strings
- user input
- printing output
- arithmetic
- conditionals
- loops

Variables are stored in a Python dictionary. This makes it easy to save
and update values while the program is running.

## Keywords and Operators

The language includes more than 8 keywords/operators.

Keywords:

- `PRINT`
- `INPUT`
- `SET`
- `ADD`
- `SUB`
- `MUL`
- `MOD`
- `LEN`
- `CHAR`
- `CONCAT`
- `IF`
- `WHILE`
- `END`

Operators:

- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`

## What Each Command Does

`PRINT value`
Prints a value to the screen.

`INPUT var`
Takes user input and stores it in a variable.

`SET var value`
Stores a value in a variable.

`ADD x y result`
Adds two integers and stores the answer in `result`.

`SUB x y result`
Subtracts `y` from `x` and stores the answer in `result`.

`MUL x y result`
Multiplies two integers and stores the answer in `result`.

`MOD x y result`
Finds the remainder when `x` is divided by `y`.

`LEN text result`
Stores the length of a string in `result`.

`CHAR text index result`
Gets one character from a string using an index.

`CONCAT x y result`
Joins two values together as text.

`IF x operator y`
Runs the lines inside the block only if the condition is true.

`WHILE x operator y`
Repeats the lines inside the block while the condition stays true.

`END`
Marks the end of an `IF` block or `WHILE` block.

## How the Interpreter Works

The interpreter follows a simple process:

1. Open the program file.
2. Read the file line by line.
3. Remove blank lines and comment lines.
4. Split each line into tokens.
5. Use the first token as the command name.
6. Execute the command.
7. Store and update variables in a dictionary.

## Main Functions Used in `interpreter.py`

`get_value(token, variables)`
This function converts a token into its real value. If the token is a
variable name, it returns the variable value. If the token is an
integer, it converts it to `int`. If the token is inside quotes, it
returns a string.

`load_program(filename)`
This function opens the `.txt` file, removes blank lines and comment
lines, and returns a clean list of program lines.

`evaluate_condition(tokens, variables)`
This function checks conditions such as `x == y`, `count > 0`, or
`number != 5`. It is used by both `IF` and `WHILE`.

`find_matching_end(lines, start_index)`
This function finds the correct `END` for an `IF` or `WHILE` block.
It also works with nested blocks.

`run_math_command(command, tokens, variables)`
This function handles the arithmetic commands `ADD`, `SUB`, `MUL`, and
`MOD`.

`execute_simple_command(line, variables)`
This function runs commands that do not create blocks, such as `PRINT`,
`SET`, `INPUT`, `ADD`, `SUB`, `MUL`, `MOD`, `LEN`, `CHAR`, and
`CONCAT`.

`execute_block(lines, variables, start_index=0, end_index=None)`
This function runs a section of the program. It is responsible for
handling `IF`, `WHILE`, and `END`.

`run_file(filename)`
This function prepares the variable dictionary, loads the program, and
starts execution.

`main()`
This function reads the filename from the command line and starts the
interpreter.

## Example Commands

Example 1:

```text
SET x 5
SET y 3
ADD x y total
PRINT total
```

Output:

```text
8
```

Example 2:

```text
INPUT name
PRINT name
```

If the user types `Alice`, the output is:

```text
Alice
```

Example 3:

```text
SET count 3
WHILE count > 0
PRINT count
SUB count 1 count
END
```

Output:

```text
3
2
1
```

Example 4:

```text
SET word "wow"
LEN word size
PRINT size
CHAR word 1 middle
PRINT middle
```

Output:

```text
3
o
```

## Required Program Files

`helloworld.txt`
Prints `hello`.

`cat.txt`
Takes user input and prints it back.

`multiply.txt`
Takes two inputs, multiplies them, and prints the result.

`repeater.txt`
Takes a character and a number, then repeats the character that many
times.

`reverse_string.txt`
Takes a string and prints the reverse.

`is_palindrome.txt`
Takes a string and prints `yes` if it is a palindrome, otherwise
prints `no`.

`is_even.txt`
Takes an integer and prints `even` if the number is divisible by 2,
otherwise prints `odd`.

## How to Run the Interpreter

From the project folder, use:

```bash
python3 interpreter.py helloworld.txt
python3 interpreter.py cat.txt
python3 interpreter.py multiply.txt
python3 interpreter.py repeater.txt
python3 interpreter.py reverse_string.txt
python3 interpreter.py is_palindrome.txt
python3 interpreter.py is_even.txt
```

## Sample Test Inputs

For `cat.txt`, type:

```text
hello
```

For `multiply.txt`, type:

```text
7
8
```

For `repeater.txt`, type:

```text
*
5
```

For `reverse_string.txt`, type:

```text
hello
```

For `is_palindrome.txt`, type:

```text
level
```

For `is_even.txt`, type:

```text
8
```

## Error Handling

The interpreter includes simple error handling so the program does not
crash easily. It checks for:

- missing files
- unknown commands
- missing command arguments
- wrong data types for math commands
- divide by zero in `MOD`
- invalid string indexes in `CHAR`
- missing `END` in `IF` or `WHILE` blocks

## Summary

This project demonstrates the basic ideas behind programming language
design and interpreter implementation. The language is small, easy to
read, and simple to explain, but it still supports variables, user
input, arithmetic, conditionals, loops, and string processing.
