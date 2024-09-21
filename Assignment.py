# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is my first line.\n")
    file.write("Here is a number: 42.\n")
    file.write("This is the third line, written on 2024-09-21.\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    contents = file.read()
    print("Contents of 'my_file.txt':")
    print(contents)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Appending this new line.\n")
    file.write("Another line added here.\n")
    file.write("Final line for this example.\n")

# Display updated content
with open("my_file.txt", "r") as file:
    updated_contents = file.read()
    print("Updated contents of 'my_file.txt':")
    print(updated_contents)
