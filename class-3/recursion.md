# Recursion
*****
Recursion is **a programming concept** where ***a function*** calls itself **directly or indirectly** to **solve a problem** by ***breaking it down into smaller***, ***more manageable subproblems**.
----
*****
 In a recursive solution, the function repeatedly applies the same logic to the smaller subproblems until it reaches **a base case, which is a condition that doesn't require further recursion.** Recursion can be a ***powerful technique for solving problems that exhibit repetitive structures or can be naturally*** defined in terms of **smaller instances of the same problem**.

There are many examples and applies for a recursive functions: [**math series repo as fibonacci luck functions**](https://github.com/doaamelhem96/math-series) 
======
These are important ideas to follow some best practices when you think about implement recursive def:

1- **Define the base case:** Every recursive function should have a base case that defines the condition under which the recursion ***stops***. ***Without a base case,*** the function would **keep calling itself indefinitely**, resulting in **infinite recursion.**

2. **Ensure progress towards the base case:** For a recursive function to terminate, each recursive call should move the problem closer to the base case. If the recursive calls don't make progress towards the base case, the function may end up in infinite recursion or **take an excessively long time to execute.**

3- **Maintain state properly:** Take care of any necessary state management within the recursive function. This includes passing and updating parameters correctly between recursive calls and handling any additional data structures or variables required to solve the problem.

3- Handle **edge cases** and **invalid inputs**: Consider how the recursive function will handle edge cases, such as the smallest possible input or ***invalid input values***. **Ensure that the function behaves correctly and gracefully handles such scenarios.**

4. Test and validate: Thoroughly **test the recursive function with different input values, including base cases and larger inputs**, to ensure correctness and efficiency.









## Things I want to know more about
