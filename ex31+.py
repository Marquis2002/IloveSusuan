from sys import argv
script, name, code = argv
prompt = '>'
if code == "123456":
    print("Welcome James, our hero!")
    print("You don't know what happened, nor the people around you.")
    print("You decide to:")
    print("1. Ask the people what happened.")
    print("2. Pretend to smile.")
    print("3. Stant up silently.")
    step1 = input(prompt)
    print("<<<<<<<< step1:", step1)

    if step1 == "1":
        print("The people burst into tears and kill you. Good job!")
    elif step1 == "2" or step1 == "3":
        print("An old saint start to mumble in a strange tone which you've never come to.")
        print("You decide to:")
        print("1. Ask the people what happened.")
        print("2. Kill the old guy.")
        print("3. Hug the old guy and cry.")
        step2 = input(prompt)
        print("<<<<<<<< step2:", step2)
        if step2 == "1" or step2 == "2":
            print("The people burst into tears and kill you. Good job!")
        elif step2 == "3":
            print("Congrtulations! You are survived the chapter1.")
        else:
            print("What a stupid man! Why did you give me a thing not number.")


    else:
        print("What a stupid man! Why did you give me a thing not number.")
else:
    print("Wrong code, you need to find the right key.")

print("This is brief game, and you don't need to care 'bout the theme.")
print("Goodbye!")


# if i == 1:
#     print(a)
# else:
#     if i == 2:
#         print(b)
#     else:
#         print(c)
#
#
#
# if i == 1:
#     print(a)
# elif i == 2:
#     print(b)
# else:
#     print(c)
