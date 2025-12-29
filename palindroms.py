def palindroms(str):
    if len(str)<=1:
        return True
    if str[0]==str[-1]:
        return palindroms(str[1:-1])
    else:
        return False
    
str=input("Enter the string:")
print("This is  palindrome:",palindroms(str))
    