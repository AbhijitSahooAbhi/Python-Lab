

with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file is used for demonstration purposes.\n")

print("Data written to 'example.txt'.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()

print("Content of 'example.txt':")
print(content)
