# PF-Prac-1
def add_string(str1):
    a = "ly"
    b = "ing"
    # start writing your code here
    if (len(str1) < 3):
        return str1
    else:
        if ("ing" in str1):
            return str1 + a
        else:
            return str1 + b

    return str1


str1 = "com"
print(add_string(str1))