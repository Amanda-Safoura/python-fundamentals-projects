if a variable exist in python

To check if a variable exists in Python, use the **`in`** operator with the **`locals()`** or **`globals()`** functions depending on the scope, or use a **`try-except`** block to catch **`NameError`**.

### 1. Check Local Scope
Use **`locals()`** to verify if a variable name exists in the current local namespace (e.g., inside a function).
```python
def check_local():
    x = 10
    if 'x' in locals():
        print("Variable 'x' exists")
    else:
        print("Variable 'x' does not exist")
```

### 2. Check Global Scope
Use **`globals()`** to verify if a variable name exists in the global namespace.
```python
y = 20
if 'y' in globals():
    print("Variable 'y' exists")
else:
    print("Variable 'y' does not exist")
```

### 3. Check Any Scope (Try-Except)
The most Pythonic approach for general existence checks is attempting to access the variable and catching the **`NameError`** if it is undefined.
```python
try:
    z
    print("Variable 'z' exists")
except NameError:
    print("Variable 'z' does not exist")
```

### 4. Check Object Attributes
For variables stored as attributes of an object or class, use the **`hasattr()`** function.
```python
class MyClass:
    my_var = 5

obj = MyClass()
if hasattr(obj, 'my_var'):
    print("Attribute 'my_var' exists")
```