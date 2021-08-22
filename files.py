# Files in python
fo = open("foo.txt", "w")
fo.write("Python is a great language.\nYeah its great!!\n")
print("Name: ", fo.name)
print("Is Closed: ", fo.closed)
print("Opening Mode: ", fo.mode)
fo.close()


fo = open("foo.txt", "r+")
str = fo.read(100)
print ("Read String is : ", str)



# check current position
position = fo.tell()
print ("Current file position : ", position)
# Close opened file
fo.close()