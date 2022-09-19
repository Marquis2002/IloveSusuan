score = 0
# Def:What to eat?
def have_meals():
    print("Baby, I'm hungry. Will we have dinner together?")
    print("1. It's up to you.")
    print("2. Huh, I've just planned to date you. You're in my stomach!")
    step = input(">")

    if step == "1":
        die("How dare you to be so careless!")
    elif "2" in step and "love" in step:
        bonus(2)
        have_meals_plus()
    elif  step == "2":
        bonus(1)
        have_meals_plus()
    else:
        die("Learn to type number!")


def have_meals_plus():
    bonus(3)
    print("Baby, you are such a sugar boy! So can you bring me a bever for the dinner?")
    print("1. Of course my sugar.")
    print("2. Well, it's harmful to drink.")
    step = input(">")

    if step == "1":
        bonus(1)
    else:
        die("Boy, try to be more lovely.")


def miss_you():
    print("Baby, I miss you so much!")
    print("Baby, why keep silent?")
    step = input(">")

    if "love" in step:
        bonus(3)
    elif "miss" in step:
        bonus(2)
    elif "honey" in step or "baby" in step:
        bonus(1)
    else:
        miss_you()


def love_you():
    print("Honey, I love you!")
    print("Your girl stare at your eyes and play your hair.")
    print("So what do you say?")
    print("1. Nope.")
    print("2. Yes.")
    step = input(">")

    if step == "1":
        die("How dare you!")
    elif step == "2":
        bonus(1)
        love_you_plus()
    else:
        die("Learn to type number!")


def love_you_plus():
    print("Why do you love me?")
    step = input(">")
    if "love" in step:
        die("Boy, there's nothing to do with love or not. Don't make this mistake next time.")
    else:
        print("Huh~ You're a bad boy. Now give me an answer, why do you love me.")
        step1 = input(">")
        if "because" in step1:
            bonus(1)
        elif "love" in step1:
            bonus(2)
        else:
            bonus(0)


# def die()
def die(str):
    global score
    score -= 1
    print(str, "Good job, sonny. You make it racket!")
# def bonus()
def bonus(i):
    global score
    score += i

def main():
    global score
    print("Now tell me your girlfriend's name.")
    name = input("> ")
    print(name, "?What a cute name!")
    print("And {} have some requests now:".format(name))
    have_meals()
    miss_you()
    love_you()
    print(f"So {name} gives you a final score: {score}.")

main()
