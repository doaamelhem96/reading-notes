1. Variable scope in Python:
In Python, variable scope refers to the part of a program in which a variable can be accessed. Python has two types of variable scopes - local and global. Local variables are those that are defined inside a function and can only be accessed within that function, while global variables are defined outside of functions and can be accessed from anywhere in the code.

Example:
```
# Local scope example
def my_function():
    x = 5
    print(x)

my_function()  # prints 5
print(x)  # raises NameError: name 'x' is not defined

# Global scope example
x = 10
def my_function():
    print(x)

my_function()  # prints 10
print(x)  # prints 10
```

2. Global and nonlocal keywords:
In Python, the global keyword is used to access global variables from within a function. When a variable is marked as global, it can be accessed and modified from anywhere in the code. The nonlocal keyword is used to access variables from an outer function within a nested function.

Example:
```
# Global keyword example
x = 5
def my_function():
    global x
    x = 10

my_function()
print(x)  # prints 10

# Nonlocal keyword example
def outer_function():
    x = 5
    def inner_function():
        nonlocal x
        x = 10
    inner_function()
    print(x)

outer_function()  # prints 10
```

3. Big O notation:
Big O notation is used in algorithm analysis to describe the time complexity of an algorithm. It is used to describe the worst-case scenario for the amount of time an algorithm takes to complete as the input size grows to infinity. The notation uses the letter O followed by a function that represents the upper bound of the algorithm's time complexity.

For example, if an algorithm takes n^2 time to complete, its time complexity can be represented as O(n^2). Big O notation is important because it helps us compare different algorithms and choose the most efficient one for a given problem.

4. Rolling Dice Example:
To simulate a dice roll in Python, we can use the random module. Here's an example code snippet:

```
import random

def roll_dice():
    return random.randint(1, 6)

# To roll the dice:
result = roll_dice()
print(result)

# To calculate the probability of rolling a specific number over a large number of trials:
num_trials = 1000000
num_successes = 0

for i in range(num_trials):
    result = roll_dice()
    if result == 6:
        num_successes += 1

probability = num_successes / num_trials
print(probability)  # should be close to 1/6 (0.1666...)
```
This code rolls a dice and returns a number between 1 and 6. We can then use a loop to roll the dice a large number of times and count the number of times we roll a 6. Finally, we divide the number of successes by the total number of trials to get the probability of rolling a 6.