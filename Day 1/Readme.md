# Day 1: Arrays and Complexity Analysis

Welcome to Day 1 of **50 Days of DSA in Python**! On this day, we focused on foundational topics, including **Complexity Analysis** and **Array** operations. This README will cover the detailed explanations and solutions to all the questions and concepts we explored.

---

## **Topics Covered**

### **1. Complexity Analysis**
Understanding the efficiency of algorithms is crucial for writing optimized code. We delved into the following concepts related to complexity analysis:

#### **What is Complexity Analysis?**
- **Complexity analysis** is the study of how the running time and space requirements of an algorithm scale with respect to the size of the input.
- It helps us predict the performance of an algorithm, particularly for larger inputs.

#### **Time Complexity**
- **Time Complexity** measures how the running time of an algorithm increases as the input size grows. It is often described using **Big O notation**.
- **Big O** notation gives an upper bound on the running time of an algorithm. For example:
  - **O(1)**: Constant time - the algorithm takes the same amount of time, regardless of input size.
  - **O(n)**: Linear time - the algorithm's time grows linearly with the input size.

#### **Asymptotic Analysis**
- **Asymptotic analysis** is a method of describing the behavior of an algorithm as the input size approaches infinity. It includes the best, worst, and average cases.
  - **Best Case**: The best scenario for the algorithm’s performance.
  - **Worst Case**: The worst scenario, usually the upper bound.
  - **Average Case**: The expected performance under normal conditions.

#### **What is Big O?**
- **Big O** is a mathematical notation used to describe the upper limit of an algorithm's running time or space usage as the input size grows. Common Big O complexities include:
  - **O(1)**: Constant time complexity.
  - **O(n)**: Linear time complexity.
  - **O(log n)**: Logarithmic time complexity, often seen in algorithms like binary search.
  - **O(n^2)**: Quadratic time complexity, common in algorithms with nested loops.

#### **Common Complexities**
- We reviewed the following common time complexities:
  - **O(1)**: The algorithm takes a constant amount of time to complete.
  - **O(n)**: The algorithm’s running time scales linearly with the input size.
  - **O(log n)**: The algorithm reduces the input size exponentially, such as in binary search.
  - **O(n^2)**: The running time increases quadratically, often seen in sorting algorithms like Bubble Sort or Selection Sort.

#### **Space Complexity**
- **Space complexity** refers to the amount of memory an algorithm needs relative to the input size.
- Like time complexity, space complexity is often expressed in terms of Big O notation.

#### **Techniques to Simplify Big O Expressions**
- To simplify Big O expressions, we focus on the **dominant term**. For example, in **O(n^2 + n)**, the **O(n^2)** term dominates as the input size grows, so the overall complexity is **O(n^2)**.

#### **Logarithms**
- **Logarithms** are commonly used in algorithms that divide the problem into smaller subproblems, such as binary search. For example, **O(log n)** represents the time complexity of an algorithm that halves the input size at each step.

---

### **2. Array Data Structure**
We explored the **Array** data structure and its various operations, which are fundamental to understanding algorithms and data structures. 

#### **What are Arrays?**
An **array** is a collection of elements, each identified by an index or key. Arrays are used to store multiple values in a single variable, and all elements in an array must be of the same type.

#### **Big O of Common Array Operations**
We discussed the Big O complexities of common operations on arrays:
1. **Access**:
   - **Description**: Accessing an element at a specific index in an array.
   - **Complexity**: **O(1)** – Constant time, since arrays allow direct access to any element by index.
   
2. **Set**:
   - **Description**: Updating an element at a specific index in an array.
   - **Complexity**: **O(1)** – Constant time, as setting an element at a given index is a direct operation.

3. **Traverse/Search**:
   - **Description**: Traversing or searching for an element in the array.
   - **Complexity**: **O(n)** – Linear time, since each element may need to be checked.

4. **Copy**:
   - **Description**: Copying an entire array to a new array.
   - **Complexity**: **O(n)** – Linear time, as each element needs to be copied.

5. **Insert**:
   - **Description**: Inserting an element at a specific index.
     - At the beginning: **O(n)** – All elements need to be shifted.
     - At the end: **O(1)** – Adding to the end is constant time.
     - In the middle: **O(n)** – Elements after the insertion point need to be shifted.

6. **Remove**:
   - **Description**: Removing an element at a specific index.
     - At the beginning: **O(n)** – Elements need to be shifted.
     - At the end: **O(1)** – Removing from the end is constant time.
     - In the middle: **O(n)** – Elements after the removal point need to be shifted.

---

### **3. Solving Problems with Arrays**
We solved two problems related to arrays, each using two different methods to improve our problem-solving skills.

#### **Problem 1: Sorting Squares**
- **Problem Statement**: Given an array of integers in which each subsequent value is not less than the previous value, return a new array with the squares of each number sorted in ascending order.
  
##### **Method 1: Brute Force Approach**
```python
def sorted_array(array):
    n = len(array)
    res = [0] * n
    for i in range(n):
        res[i] = array[i] ** 2
    res.sort()
    return res
```
- Explanation: This method squares each element of the array and sorts the results.
- Time Complexity: O(n log n) due to the sorting step.
- Space Complexity: O(n) due to the new array res.

##### **Method 2: Optimized Approach**
```python
def sorted_array(array):
    n = len(array)
    i, j = 0, n - 1
    res = [0] * n
    for k in reversed(range(n)):
        if array[i] ** 2 > array[j] ** 2:
            res[k] = array[i] ** 2
            i += 1
        else:
            res[k] = array[j] ** 2
            j -= 1
    return res
```
- Explanation: This method uses two pointers, starting from both ends of the array. It compares the squares and inserts the larger value at the correct position in the result array.
- Time Complexity: O(n) due to the single pass through the array.
- Space Complexity: O(n) for the result array.

#### **Problem 2: Monotonic Array **
- **Problem Statement**: Determine if the given array is monotonic (either non-decreasing or non-increasing).
```python
def monotonic_array(array):
    n = len(array)
    if n == 0:
        return True
    first = array[0]
    last = array[n - 1]
    if first > last:
        for k in range(n - 1):
            if array[k] < array[k + 1]:
                return False
    elif first == last:
        for k in range(n - 1):
            if array[k] != array[k + 1]:
                return False
    else:
        for k in range(n - 1):
            if array[k] > array[k + 1]:
                return False
    return True
```
- Explanation: This method checks if the array is either strictly increasing or decreasing by comparing elements from left to right.
- Time Complexity: O(n) as the array is traversed once.
- Space Complexity: O(1) since we only use a few variables.

## Conclusion

In **Day 1**, we covered essential topics that will serve as the foundation for the next 49 days of learning. The combination of understanding algorithm complexity and mastering fundamental data structures like arrays will be key to solving more complex problems in the coming days.

We are now ready to move on to the next set of topics, continuing to improve our skills in **Data Structures and Algorithms**.

---

## Next Steps

In the following days, we will explore more data structures and algorithms, including:
- Linked lists
- Stacks
- Queues
- Sorting algorithms
- And much more...

We will continue practicing problems to enhance our problem-solving ability and improve our Python skills.

Stay tuned for more detailed explanations and solutions!


This **README.md** file covers all the topics, problems, and solutions you worked on during **Day 1** of your 50-day DSA journey. It includes detailed descriptions, code explanations, and Big O complexities for each problem and concept you explored.