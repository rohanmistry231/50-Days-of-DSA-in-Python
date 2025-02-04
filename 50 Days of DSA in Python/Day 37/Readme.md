# **Day 37: Stacks**

Welcome to Day 37 of **50 Days of DSA in Python**! Today, we explore **Stacks**, a fundamental data structure that follows the **Last In, First Out (LIFO)** principle. We will cover the **construction of a stack** and how to evaluate **Reverse Polish Notation (RPN)** using stacks. Stacks are widely used in expression evaluation, undo operations, and parsing algorithms.

---

### **Topics Covered:**
- Stacks  
- Construct Stack  
- Reverse Polish Notation  

---

## **1. Constructing a Stack**

### **Problem Statement**  
A stack is a linear data structure where elements are added and removed from the same end, called the "top" of the stack. The basic operations of a stack are:
- **push**: Add an element to the stack
- **pop**: Remove the top element
- **peek**: View the top element without removing it
- **is_empty**: Check if the stack is empty

### **Approach**

#### **1. Implementing Stack Using Python List**

In Python, stacks can be easily implemented using lists. We use the `append` method to push elements onto the stack and `pop` method to remove the top element. The `peek` operation is done by accessing the last element, and `is_empty` can be checked using `len()`.

#### **Code:**
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack. Raises an error if the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """
        Return the top item without removing it.
        """
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.stack) == 0
```

---

## **2. Reverse Polish Notation (RPN)**

### **Problem Statement**  
Reverse Polish Notation (RPN) is a mathematical notation in which every operator follows all of its operands. It eliminates the need for parentheses to denote precedence of operators. For example, the expression `3 + 4` in RPN would be written as `3 4 +`. We will use a stack to evaluate expressions in RPN.

### **Approach**

#### **1. Evaluating RPN Using Stack**

To evaluate an RPN expression:
1. Loop through each token (number or operator).
2. If the token is a number, push it onto the stack.
3. If the token is an operator, pop the two numbers from the stack, apply the operator, and push the result back onto the stack.
4. After processing all tokens, the stack should contain only one element, which is the final result.

#### **Code:**
```python
def evaluate_rpn(expression):
    """
    Evaluate an expression in Reverse Polish Notation (RPN).
    
    Args:
        expression (List[str]): List of tokens representing an RPN expression.
        
    Returns:
        int: The result of the RPN expression.
    """
    stack = []

    for token in expression:
        if token in ('+', '-', '*', '/'):
            # Pop the top two elements from the stack
            b = stack.pop()
            a = stack.pop()

            # Perform the operation based on the operator
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Integer division
        else:
            # If the token is a number, push it to the stack
            stack.append(int(token))

    return stack[0]  # The result is the only element remaining in the stack
```

### **Example:**

```python
expression = ["2", "1", "+", "3", "*"]
print(evaluate_rpn(expression))  # Output: 9
```

In the above example:
- `2 1 +` results in `3`
- `3 * 3` results in `9`

---

### **Conclusion**

Today, we explored **Stacks** and applied them to two important problems:

1. **Constructing a Stack**: We implemented a basic stack with operations like `push`, `pop`, `peek`, and `is_empty`.
   
2. **Reverse Polish Notation (RPN)**: We used a stack to evaluate expressions in RPN, following a straightforward algorithm to handle operators and operands.

By mastering these concepts, you will be equipped to solve problems involving expression evaluation, balancing symbols, and more. Keep practicing, and we’ll continue to cover more data structures and algorithms in the coming days!