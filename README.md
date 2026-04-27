# Simple Custom Language

This project is a very simple interpreted language written in Python.
The interpreter reads a `.txt` file line by line, splits each line into
tokens, and uses the first token as the command name.

## Main Features

- Variables stored in a Python dictionary
- Integer and string values
- User input with `INPUT`
- Output with `PRINT`
- Arithmetic with `ADD`, `SUB`, `MUL`, and `MOD`
- String helpers with `LEN`, `CHAR`, and `CONCAT`
- Conditionals with `IF`
- Loops with `WHILE`
- Block ending with `END`

## Keywords and Operators

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

## How It Works

Each line in a program file is one command.
Example:

```text
SET x 5
ADD x 3 result
PRINT result
```

The interpreter keeps all variables in a dictionary and safely handles
basic errors so the program does not crash easily.
