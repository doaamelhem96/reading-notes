# Intro to Data Structure
In computer science, a linear data structure refers to a data structure in which elements are arranged sequentially, and each element has a unique predecessor and successor, except for the first and last elements. Common examples of linear data structures include arrays, linked lists, queues, and stacks.
***
# Big (o)
The time complexity of operations performed on a linear data structure depends on the specific implementation and the operation being performed.
****
Here are the typical time complexities associated with common operations on linear data structures:

Accessing an element by index:

Arrays: O(1)
Linked lists: O(n)
Queues and stacks: O(n) or O(1), depending on whether accessing the front or top element.
Insertion/Deletion at the beginning:

Arrays: O(n)
Linked lists: O(1)
Queues and stacks: O(1)
Insertion/Deletion at the end:

Arrays (with dynamic resizing): Amortized O(1)
Linked lists: O(1)
Queues and stacks: O(1)
Insertion/Deletion at an arbitrary index:

Arrays: O(n)
Linked lists: O(n)
Queues and stacks: Not applicable (not typically supported)
Searching for an element:

Arrays: O(n)
Linked lists: O(n)
Queues and stacks: O(n)

#### In summary, the time complexity of operations on linear data structures can vary depending on the specific implementation. Generally, accessing elements by index or performing operations at the beginning or end can have different time complexities across different linear data structures. It's important to consider the requirements of your application and choose the appropriate linear data structure accordingly.

# things i want to learn