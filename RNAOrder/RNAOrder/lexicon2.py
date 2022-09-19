from random import choice
a = input("Please enter the first thing.")
b = input("Please enter the second thing.")
c = input("Please enter the third thing.")
n = int(input("Please enter the amount of RNA order needed."))

i = 0
while i < n:
    list = [a, b, c]
    arr = [choice(list) for i in range(0, 17)]
    ans = ''.join(arr)
    print(ans)
    i += 1