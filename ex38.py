ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not ten things in that list. Let's fix that.")

# split(ten_things, ' ')
stuff = ten_things.split(' ')

more_things = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_things)
    next_one = more_things.pop()
    print("Adding:", next_one)
    # append(stuff, next_one)
    stuff.append(next_one)
    # format("There are {} items now.", stuff)
    print("There are {} items now.".format(len(stuff)))

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
# pop(stuff)
print(stuff.pop())
# join(' ', stuff)
print(' '.join(stuff)) # what? cool!
# join('#', stuff[3:6])
print('#'.join(stuff[3:6])) # super stellar
# join(" #", stuff[3：6])
print(' #'.join(stuff[3:6])) # super stellar
