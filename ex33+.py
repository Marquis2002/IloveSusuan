print("Please enter a number: ")
maximum = int(input('>'))

def a_while_function(max):
    i = 0
    while i < max + 1:
        print("Now we have a number", i)
        if i < max:
            print("And now we need to wait for it becoming bigger")
        i = i + 1
    print("Wow, now we have the largest one!")
    
a_while_function(maximum)
