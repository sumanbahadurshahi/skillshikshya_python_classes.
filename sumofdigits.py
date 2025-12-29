def sum_of_digit(n):
    if n<10:
        return n
    else:
       return n%10+sum_of_digit(n//10)


n=int(input("Enter the number:"))
print(f"The of digits={n} is:",sum_of_digit(n))