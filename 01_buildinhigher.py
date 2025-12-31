#buildin higher order functon
def square(num):
    return num **2

numbers=[1,2,4,5]
square_num=map(square,numbers)
print(list(square_num))

def even(num):
  return num%2==0
     

number=[2,4,6,3]
even_num=map(even,number)
print(list(even_num))


#take a list and print it into uppercase using build in higher order functon

def upper(name):
   return name.upper()

name=['suman','hari','shyam']
upper_case=map(upper,name)
print(list(upper_case))


def upper(name):
   return str.capitalize(name)

name=['suman','hari','shyam']
upper_case=map(upper,name)
print(list(upper_case))

#find the sum of each nested list and return true or false if sum is greater than 10  using map function

def check_sum(sublist):
   return sum(sublist)>10

nested_list=[[1,2,3],[4,5,6],[7,8,9]]
filter_list=map(check_sum,nested_list)

print(list(filter_list))

#filter bhaneko hataunu ..what is the different between the filter and map
# ...............................

#filter out the dictonary item based on some condition like 'name' key length greter than 3 .we know
# The filter() function in Python is another higher-order function, like map(). It’s used to select items from a 
# list (or any iterable) that satisfy a condition.
# filter always return true or false
#in dictonary key chahi tyo function ma jado rahixa.

data=[
   {'name':'suman','age':14,'lacation':'bhainsepati'},
    {'name':'Rambahadur','age':14,'lacation':'lagankhel'},
     {'name':'ram','age':14,'lacation':'magargaun'}
]

def check(item):
   return len(item['name'])>5

filter_data=filter(check,data)
print(list(filter_data))
#reduce function...herum ctr+click
from functools import reduce
# it reduce the len
#double argument 1st +2nd
def add(x,y):
   return x+y

numbers=[1,2,3,4,5]
sum_of_numbers=reduce(add,numbers)
#[3,3,4,5]
#[6,4,5]
# [10,5]
# [15]
print(sum_of_numbers)

def g(x,y):
   return max(x,y)


numbers=[3,5,6,7,8]
gratest_num=reduce(g,numbers)
print("The greatest number is :",gratest_num)

   
     


     

