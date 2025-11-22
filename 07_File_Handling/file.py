# Read File Example

file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()

# Write File Example
file = open("demo-file.txt", "w")
file.write("Hello, World!")
file.close()

# Append File Example
file = open("demo-file.txt", "a")
file.write("\nAppended Line.")
file.close()

# Reading Specific Characters
file = open("demo.txt", "r")
data = file.read(5)
print(data)
file.close()

# Line by Line Read
file = open("demo-file.txt", "r")
for line in file:
    print(line.strip())
file.close()


# Using 'with' statement for better file handling
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)
