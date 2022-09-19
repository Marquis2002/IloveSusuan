numbers = []
arg1 = int(input('Enter a number:'))
for i in range(0, arg1):
    print("Numbers at the top: ", numbers)
    print("And we get a number", i)
    numbers.append(i)
    print("Numbers at the bottom: ", numbers)
    # i = i + 1

print("See, what do we get now?")
input(">")
print("Now we get numbers", numbers)

print("In it we have elements: ")
input(">")
for i in range(0, arg1):
    print(numbers.pop(0))
