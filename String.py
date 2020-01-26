#This is a sample program containing maximum operations that can be performed using strings
user_input=str(input())
a=str.upper(user_input) # Making it Upper Case
print(a)
b=str.lower(user_input) # Making it Lower Case
print(b)
c=user_input[1:]        #Slicing
print(c)
d=user_input[1:3]
print(d)
print(len(user_input))  #Length of String
if ("a" in user_input):
    print("Wow found a in Your input")
e=user_input.find("b")  #Finds the value
print(e)
f=user_input.capitalize() #Capitalizes First Letter
print(f)
g=user_input.isalpha()   #Checks for alphabet
print(g)
h=type(user_input)      #Checks for type and returns type
print(h)
i=user_input.replace("a","i") #Replace a Value with another
print(i)
j=user_input.swapcase()   #Shifts lower to upper and upper to lower
print(j)
j=user_input.endswith("r") #Checks for the end Value
print(j)

#Happy Coding