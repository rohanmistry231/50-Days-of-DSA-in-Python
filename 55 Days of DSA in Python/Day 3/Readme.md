# Day 3: Recursion and Problem Solving

Welcome to Day 3 of **55 Days of DSA in Python**! On this day, we explored **Recursion** and addressed two fascinating problems: **Tower of Hanoi** and the **Power Sum**. This README is designed to provide a thorough understanding of these topics, including their solutions.

---

## **Topics to be Covered**

- Recursion  
- Tower of Hanoi  
- Power Sum  

---

### **[Day 3](./Day%203):**

#### Recursion
Recursion is a fundamental concept in computer science where a function calls itself to solve smaller subproblems of a larger problem. It is particularly useful in scenarios where the problem can be divided into similar subproblems, such as in the case of divide-and-conquer algorithms. 

In the context of the Tower of Hanoi problem, recursion helps us break down the problem of moving `n` disks from one rod to another into smaller problems of moving `n-1` disks. Recursion simplifies the logic but requires careful consideration of the base case (when recursion stops) and recursive case (how the function calls itself).

Key Points of Recursion:
- **Base Case**: Prevents infinite recursion by defining a condition where the function stops calling itself.
- **Recursive Case**: Defines how the problem can be solved by reducing it to smaller instances of the same problem.
- **Stack Usage**: Recursive calls are stored in the program's call stack, which can lead to stack overflow if the recursion depth is too high.

---

#### Tower of Hanoi
The Tower of Hanoi is a classic problem that demonstrates recursion's power and elegance. The objective is to move a set of disks from one rod to another, following these rules:
1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or on an empty rod.

**Recursive Solution**:
The solution to the Tower of Hanoi problem is built around the idea of moving `n-1` disks to an auxiliary rod, moving the `nth` disk to the target rod, and then moving the `n-1` disks from the auxiliary rod to the target rod.

Here is the Python implementation of the Tower of Hanoi problem:

```python
def tower_of_hanoi(n_disks, source, target, auxiliary):
    """
    Solves the Tower of Hanoi problem and prints the moves.

    Args:
        n_disks (int): The number of disks to move.
        source (int): The source rod.
        target (int): The target rod.
        auxiliary (int): The auxiliary rod.

    Returns:
        int: The total number of moves performed.
    """
    move_count = 0

    def solve_hanoi(n, source_rod, target_rod, aux_rod):
        """
        Recursive helper function to solve the Tower of Hanoi problem.

        Args:
            n (int): Number of disks to move.
            source_rod (int): The source rod.
            target_rod (int): The target rod.
            aux_rod (int): The auxiliary rod.
        """
        nonlocal move_count
        if n == 1:
            move_count += 1
            print(f"Move disk {n} from rod {source_rod} to rod {target_rod}")
            return

        # Move n-1 disks from source to auxiliary using target as auxiliary.
        solve_hanoi(n - 1, source_rod, aux_rod, target_rod)
        
        # Move the nth disk from source to target.
        move_count += 1
        print(f"Move disk {n} from rod {source_rod} to rod {target_rod}")

        # Move n-1 disks from auxiliary to target using source as auxiliary.
        solve_hanoi(n - 1, aux_rod, target_rod, source_rod)

    solve_hanoi(n_disks, source, target, auxiliary)
    return move_count
```

**Time Complexity**:
- The recursive solution has a time complexity of \( O(2^n) \), where \( n \) is the number of disks. This is because each call to the function spawns two additional recursive calls until the base case is reached.

**Space Complexity**:
- The space complexity is \( O(n) \) due to the recursion stack, where \( n \) is the number of disks.

---

#### Power Sum
The Power Sum problem involves calculating the sum of elements in a nested list, with each level of nesting contributing a progressively higher power to the sum. The solution is implemented using recursion to process nested lists.

Here is the Python implementation:

```python
def power_sum(array, power=1):
    """
    Calculate the power sum of a nested list.

    The function recursively processes nested lists, summing elements
    at increasing power levels for each level of nesting.

    Parameters:
        array (list): A list of integers or nested lists.
        power (int, optional): The power level for the current recursion. Defaults to 1.

    Returns:
        int: The power sum of the input list.
    """
    total = 0  # Variable to store the running total

    for item in array:
        if isinstance(item, list):  # Check if the current element is a list
            total += power_sum(item, power + 1)
        else:
            total += item

    return total ** power
```

**Explanation**:
- The function traverses the list recursively, checking whether each element is a nested list.
- For each nested list, the recursion depth increases, and the power is incremented.
- The base case is when the element is not a list, in which case it contributes directly to the sum.

**Example**:
```python
nested_list = [1, [2, 3], [[4]], 5]
result = power_sum(nested_list)
print(result)  # Output depends on the nesting depth and the values in the list.
```

**Complexity**:
- Time Complexity: \( O(n) \), where \( n \) is the total number of elements in the nested structure.
- Space Complexity: \( O(d) \), where \( d \) is the depth of the nested list, due to the recursion stack.

---

#### Conclusion
Day 3 provided insights into:
1. **Recursion**: Understanding its role in solving problems like Tower of Hanoi and Power Sum.
2. **Tower of Hanoi**: A classic recursion problem, highlighting the elegance and challenges of recursive solutions.
3. **Power Sum**: Demonstrating the versatility of recursion in handling complex data structures like nested lists.

These concepts strengthen the foundation of recursion, a crucial technique in problem-solving and algorithm design.