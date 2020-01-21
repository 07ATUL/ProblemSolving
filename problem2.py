# PF-Prac-2
def bracket_pattern(input_str):
    a = 0
    b = 0
    # Remove pass and write your code here
    if (input_str[0]!=input_str[len(input_str)-1] and (input_str[0] or input_str[len(input_str)-1] !=0)):
        a=input_str.count("(")
        b=input_str.count(")")
        if (a == b):
            return True
        else:
            return False

    else:
         return False

input_str = "()"
print(bracket_pattern(input_str))