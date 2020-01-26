#This is a A Problem to Check if a Number is a Palindrome or not and i am practising it from geeeks for geeks
def reverse(s):
    return s[::-1]
def isPalindrome(s):
    rev=reverse(s)
    if(s==rev):
        return True
    else:
        return False

# Method 2
def palindrome(s):
    check=''.join(reverse(s))
    if(s==check):
        return True
    else:
        return False
s=str(input())
b=isPalindrome(s)
print(b)
c=palindrome(s)
print(c)