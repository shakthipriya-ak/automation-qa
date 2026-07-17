# Day 04 - Python Functions, Exception Handling & File Handling

## Topics Covered

### 1. print() vs return

- `print()` displays the output on the screen.
- `return` sends the value back to the caller.
- If a function has no `return`, Python returns `None`.

Example:

```python
def add(a, b):
    print(a + b)

x = add(10, 20)

print(x)
```

Output:

```
30
None
```

---

### 2. Functions

- Parameters
- Arguments
- Function execution flow
- Storing returned values in variables

Example:

```python
def multiply(a, b):
    print(a * b)
    return a * b

x = multiply(2, 5)

print(x)
```

Output:

```
10
10
```

---

### 3. Exception Handling

Used to prevent programs from crashing when an error occurs.

Syntax:

```python
try:
    # Code
except:
    # Handle error
```

Example:

```python
try:
    print(10 / 0)
except:
    print("Cannot divide by zero")
```

---

### 4. File Handling

#### Read Mode (`r`)

```python
file = open("demo.txt", "r")
print(file.read())
file.close()
```

#### Write Mode (`w`)

```python
file = open("demo.txt", "w")
file.write("Automation Testing")
file.close()
```

- Overwrites existing content.

#### Append Mode (`a`)

```python
file = open("demo.txt", "a")
file.write("\nPython")
file.close()
```

- Adds content without deleting existing data.

---

### 5. read() vs readline()

`read()`

- Reads the entire file.

```python
print(file.read())
```

`readline()`

- Reads only one line at a time.

```python
print(file.readline())
```

---

### 6. with open()

Recommended way to open files.

```python
with open("demo.txt", "r") as file:
    print(file.read())
```

- Automatically closes the file.

---

### 7. strip()

Removes unwanted spaces and newline characters.

```python
line = file.readline().strip()
print(line)
```

---

### 8. Current Working Directory

```python
import os

print(os.getcwd())
```

Used to check where Python is looking for files.

---

## Important Learnings

- Difference between `print()` and `return`
- Python returns `None` when no `return` is present.
- `try-except` prevents program crashes.
- `"r"` → Read
- `"w"` → Write (Overwrite)
- `"a"` → Append
- `read()` reads the whole file.
- `readline()` reads one line.
- `.strip()` removes `\n`.
- `with open()` automatically closes files.
- File paths depend on the Current Working Directory (`os.getcwd()`).

---

## Practice Completed

- ✔ Predicting function outputs
- ✔ Understanding `print()` vs `return`
- ✔ Handling `ZeroDivisionError`
- ✔ Reading files
- ✔ Writing files
- ✔ Appending data
- ✔ Understanding `FileNotFoundError`
- ✔ Using `readline()` and `.strip()`

---

## Status

✅ Day 04 Completed