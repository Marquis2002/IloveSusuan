def while_function(arg1, arg2):
    i = 0
    numbers = []
    while i < arg1:
        print("At the top i is {}".format(i))
        numbers.append(i)
        i = i + arg2
        print("Numbers now:", numbers)
        print("At the bottom i is {}".format(i))
    print("The numbers:", numbers)
    for num in numbers:
        print(num)

while_function(99,2)
