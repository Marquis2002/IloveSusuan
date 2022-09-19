# assign 10 to types_of_people
types_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

# assign the string to binary
binary = "binary"
# assign the string to do_not
do_not = "don't"
# assign the f-string to y (insert binary and do_not in the string)
y = f"Those who know {binary} and those who {do_not}"
print("<<<<<<after assign y", y)

print(x)

print("<<<<<<before printing y", y)

print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
