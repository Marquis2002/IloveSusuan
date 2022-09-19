import random
# A game of kill more
# 0. database
creatures = {}
score = 0
grade = 1
# 1. kill() score++
def kill_or_not():
    # print(">>>>>>enter kill_or_not")
    global creatures
    # print(">>>>>>>>> creatures= ", creatures)
    
    for creature, hp in list(creatures.items()):
        # print(f"{creature}'s hp is {hp}, and hp <= 0 is {int(hp) <= 0}")
        if int(hp) <= 0:
            del creatures[creature]
            bonus_value = random.randint(1, 6)
            bonus(bonus_value)
            if creatures == {}:
                die("You have killed all creatures before getting enough score.")
            
        else:
            pass

    print(f"There are still {len(creatures)} creatures alive")
    attack()
# 2. upgrade() if score/exp > grade: grade++
def upgrade_or_not():
    global score, grade
    if score / 10 >= grade:
        grade += 1
        gen()
        win_or_not()
        upgrade_or_not()
    else:
        pass 
# 3. gen() generate new creatures
def gen():
    precreatures = ["ox", "boar", "crocodile", "lion", "tiger", "bear"]
    global creatures
    namelist = random.sample(precreatures, random.randint(1, 6))
    for name in namelist:
        hp = random.randint(1, 6)
        creatures.update({name: hp})
    namelist = []

# 4. bonus() will return the expected score
def bonus(i):
    global score, grade
    score += i
    upgrade_or_not()
    print(f">>>>>>Now your grade is {grade}, your score is {score}.")

# 5. attack() 
def attack():
    global grade
    print("Which creature will you attack?")
    print(creatures)
    name = input("> ")
    creatures[name] -= grade
    kill_or_not()

# 6. die()
def die(str):
    print("You could have done better! ", str)
    print(f"Your final grade is {grade}, and your final score is {score}.")
    exit(0)

# 7. win_or_not()
def win_or_not():
    if grade >= 10:
        print("You have become the god of this game!")
        print("Congratulations!")
        print("And now all the creatures submit to you, becoming your pet!")
        print("Please give them names.")
        pets = []
        for creature, hp in list(creatures.items()):
            print(f"So you want to give {creature} a name:")
            pets.append(input("> "))
        print(f"Now you have {len(creatures)} pets.")
        print("They are: ", pets)
        exit(0)
    else:
        pass

# main def
def main():
    print("hello")
    gen()
    attack()

# Here we go!
print("Welcome, my bravior!")
main()