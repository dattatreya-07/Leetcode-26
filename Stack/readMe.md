# Intuition
A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. The last element added to the stack is the first one to be removed. In Python, a stack can be implemented efficiently in multiple ways depending on performance needs, primarily using built-in lists or the `collections.deque` class.

# Approach
There are three standard ways to implement a stack in Python:
1. **Using a Built-in List**: The simplest way. You use `.append()` to push items and `.pop()` to remove the topmost item. However, lists can run into O(n) re-allocation overhead when they grow.
2. **Using `collections.deque`**: The most recommended and pythonic way. Built over a doubly-linked list, it guarantees O(1) time complexity for both push and pop operations regardless of size.
3. **Using `queue.LifoQueue`**: Useful in multi-threaded environments as it provides thread-safe operations, though it comes with higher performance overhead due to locking mechanisms.

# Complexity
- Time complexity:
  - Push (Insertion): \[O(1)\] for `deque`, amortised \[O(1)\] for `list`.
  - Pop (Deletion): \[O(1)\] for `deque`, amortised \[O(1)\] for `list`.
  - Peek (View top element): \[O(1)\] using index access `[-1]`.

- Space complexity:
  - Total space: \[O(n)\] where n is the number of elements stored in the stack.

# Code
```python []
# -------------------------------------------------------------
# Approach 1: Using collections.deque (Recommended for standard use)
# -------------------------------------------------------------
from collections import deque

class StackDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)  # O(1) time

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()  # O(1) time

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]    # O(1) time

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -------------------------------------------------------------
# Approach 2: Using standard built-in List (Simplest approach)
# -------------------------------------------------------------
class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # Amortised O(1) time

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()  # Amortised O(1) time

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]    # O(1) time

    def is_empty(self):
        return len(self.stack) == 0


# Example usage:
if __name__ == "__main__":
    my_stack = StackDeque()
    my_stack.push("A")
    my_stack.push("B")
    my_stack.push("C")
    
    print(f"Top element (Peek): {my_stack.peek()}") # Output: C
    print(f"Popped element: {my_stack.pop()}")     # Output: C
    print(f"Is stack empty?: {my_stack.is_empty()}") # Output: False
```
