#return true if the order of the parentheses is valid
def valid_parentheses(parentheses_str):
    if parentheses_str[0] != "(" or parentheses_str[-1] != ")":
        return False
    return True


valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False