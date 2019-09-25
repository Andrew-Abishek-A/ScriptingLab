import numpy as np
from numpy import matlib


list1 = [1, 2, 3, 4]

# length using len()
length = len(list1)
print(length)

# replacing first element of list1 with a list list2
list2 = [1, 2, 3]
list1[0] = list2
print(list1)

# Slice operator
sobj = slice(0, 3, 2)
print(list1[sobj])

# Replacing the 2nd element with a fruit name
list1[1] = "some_fruit_name"
print(list1)

# Concatenate 2 lists
list3 = list1+list2
print(list3)

# Cloning a list
list_clone_1 = list1
list_clone_2 = list(list1)
list_clone_3 = np.matlib.repmat(list1, 1, 1)
print(list_clone_1, list_clone_2, list_clone_3)

# Splitting a list
split_list1 = list1[0:int(len(list1)/2)]
split_list2 = list1[int(len(list1)/2):]
print(split_list1, split_list2)


# Create a tuple with numbers
tuple1 = (1, 2, 3, 4)
print(tuple1[2])

# convert tuple to list
tuple_list1 = list(tuple1)
print(tuple_list1)
