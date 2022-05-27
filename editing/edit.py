# opening and editing files in python
role_file=open("roles.txt" , "r")
print(role_file.readline())

#close file
role_file.close()

# Read
file=open("./roles.text" , "r")
words=file.read()
print(words)
file.close()

# Write
file=open("./roles.txt" ,"a")
file.write("i love pyton")
file.close()