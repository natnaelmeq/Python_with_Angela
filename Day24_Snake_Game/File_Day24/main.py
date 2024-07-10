with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file: #if only mode can write if it "r" only read, and "a" append
    file.write("\n100 days of python challenge exciting")
    print(contents)