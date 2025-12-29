def find_smallest(lst):
    if len(lst)==1:
        return lst[0]
    smallest=find_smallest(lst[1:])
    if lst[0]<smallest:
        return lst[0]
    else:
        return smallest
    
    
numbers=[5,2,9,1,7]
print("The smallest number is:",find_smallest(numbers))
