# hairs = ['brown', 'blond', 'red']
# print(">>>>>>hairs", hairs)
#
# eyes = ['brown', 'blue', 'green']
# print(">>>>>>eyes", eyes)
#
# weights = [1, 2, 3, 4]
# print(">>>>>>weights", weights)
#
# list = [hairs, eyes, weights]
# print(">>>>>>list", list)


# this exercise use list.append() and range(), alsp for-loop

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2,'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit or type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since wo don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []
# elements = range(0, 6)
# then use the range function ro do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
