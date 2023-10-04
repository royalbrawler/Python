import os
import sys
# r = Read
# a = Append
# w = Write
# x = Create

currentPath = os.path.dirname(__file__)
def my_get_path(filename): return os.path.join(currentPath, filename)

# Read - error if it doesn't exist

# list all files current directory
# for z in os.listdir(os.path.dirname(__file__)):
#     print(z)


# f = open("names.txt")
# f = open("names.txt", "rt")  # .. rt - read text file // rb - read binary file
# f = open(currentPath + "/names.txt")
f = open(my_get_path("names.txt"))

print(f.read())  # read all
print(f.read(4))  # read first 4 characters

print(f.readline())
print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names_inexistent.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")  # a - append
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# 1-Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# 2-Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")  # x - create
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")


# [ with ] has built-in implicit exception handling
# close() will be automatically called
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
