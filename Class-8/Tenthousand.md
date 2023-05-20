1. Python List Comprehension:
List comprehension is a concise way to create lists in Python. It allows you to create a new list by iterating over an existing iterable (such as a list, tuple, or string) and applying an expression or condition to each element. The basic syntax of a list comprehension is as follows:

```python
new_list = [expression for element in iterable if condition]
```

- `new_list`: The resulting list created from the comprehension.
- `expression`: The operation or transformation applied to each element.
- `element`: The current element from the iterable.
- `iterable`: The existing iterable to iterate over.
- `condition` (optional): A condition that filters the elements before applying the expression.

Example:
Let's say we have a list of integers and we want to create a new list that contains the squares of each element. We can use a list comprehension to achieve this:

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

2. Decorators in Python:
Decorators are a feature in Python that allow you to modify the behavior of a function or class without changing its source code. They are functions that wrap another function, adding some functionality before, after, or around the wrapped function. Decorators use the `@decorator_name` syntax and can be applied to functions or classes.

Decorators provide a way to extend or modify the behavior of functions or classes without directly modifying their implementation. They are commonly used for tasks such as logging, input validation, authentication, and timing.

Example:
Here's a simple example of a decorator that logs the function name before and after it is called:

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished calling function: {func.__name__}")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("John")
```

Output:
```
Calling function: greet
Hello, John!
Finished calling function: greet
```

In this example, the `log_decorator` wraps the `greet` function, adding logging statements before and after its execution. The `@log_decorator` syntax applies the decorator to the `greet` function, so whenever `greet` is called, it will go through the wrapper function defined in the decorator.