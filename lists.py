list1 = ['Zaryab', 23, 5.9, 'Pakistan']

for element in list1:
    print(element)
print('\n')
# Accessing value in a list
print(list1[0])
print(list1[0:3])

# Updating list
list1[0] = 'Ali'
list1[1] = 22
list1[2] = 6.3
print(list1)

# Deleting list elements\
del list1[2]
print(list1)

# Inserting elements in the last of list
list1.insert(len(list1)+1, 'Arya')
print(list1)