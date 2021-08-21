# Dictionary
dict = {'Name': 'Zaryab', 'Age': 23, 'State': 'Pakistan'}

print(dict['Name'])
print(dict['Age'])

# Updating Dictionary
dict['Age'] = 24
print(dict)

# Adding to Dictionary
dict['City'] = 'Karachi'
print(dict)

# Delete Dictionary Elements
del dict['Age']
print(dict)

# Dictionary Length
print(len(dict))

# Dictionary Keys
print(dict.keys())

# Dictionary Values
print(dict.values())

# Dictionary Items
print(dict.items())

# Dictionary Iteration
for key in dict:
    print(key)
