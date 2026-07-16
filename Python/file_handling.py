with open("demo.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
with open("demo.txt", "r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())
print()
with open("demo.txt", "r") as file:
    print(file.readline(),end='')
    print(file.readline(),end='')
    print(file.readline(),end='')
text = "Hello\n"

print(text)
print(text.strip())