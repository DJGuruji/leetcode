def isValid(s: str) -> bool:
    stack = []
    # Define matching pairs
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    return not stack

if __name__ == "__main__":
    s = "({{[]}})"
    print(isValid(s))
