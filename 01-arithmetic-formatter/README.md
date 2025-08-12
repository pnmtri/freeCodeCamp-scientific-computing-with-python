# Arithmetic_Formatter #
Python Project (problem provided by freeCodeCamp.org - from Scientific Computing with Python course)

**Arithmetic Formatter**
Arithmetic Formatter is a Python function that arranges simple addition and subtraction problems into a clean vertical format. It follows strict formatting and validation rules, similar to how math problems are written in school. You can also choose to show or hide the answers.

**Features**
Accepts up to 5 arithmetic problems

Supports only + and - operators

Checks that all numbers contain only digits

Each number must be no more than 4 digits long

Aligns problems vertically with proper spacing

Optional display of calculated answers (show_answers=True)

**Example**
python
Copy
Edit
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
**Note**
The function will return error messages for invalid input (too many problems, unsupported operators, long numbers, or non-digit characters).

Here is how I planned up the coding, the ideation step, for the project before starting anything on computer:
<img width="2048" height="1536" alt="image" src="https://github.com/user-attachments/assets/b2950c32-a7a0-420d-9ed0-33e5681fee7d" />

## How to run
```bash
python main.py
