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
