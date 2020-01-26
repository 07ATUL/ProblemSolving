# To Calculate the matching characters in a given string and return its value
def matched(input1,input2):
    set_1=set(input1)
    set_2=set(input2)
    b=set_1 & set_2
    return str(len(b))
input_1=str(input())
input_2=str(input())
match=matched(input_1,input_2)
print(match)