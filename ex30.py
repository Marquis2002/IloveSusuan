# define three valuables, and give them values.
people = 30
cars = 40
trucks = 15

# begin the if block
if cars > people:
    print("We should take the cars.")
# else if
elif cars < people:
    print("We should not take the cars.")
# else
else:
    print("We can't decide.")
#another if block
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("Still we can't decide.")
#another if block
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
