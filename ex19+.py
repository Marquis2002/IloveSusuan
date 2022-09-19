prompt = '>'
print("This script will show how much more James love Susan than Susam does.")
filename = "love.txt"

def showlove():
    love_amount_Susan = 0
    love_amount_James = 0
    #print("<<<<<<<< love_amount_Susan = ",love_amount_Susan,"<<<<<<<<<<<<<<<<<love_amount_James = ", love_amount_James)
    print("Plese enter a number to estimate how much Susan love James:")
    love_amount_Susan = int(input(prompt))
    print("<<<<<<<< love_amount_Susan = ",love_amount_Susan,"<<<<<<<<<<<<<<<<<love_amount_James = ", love_amount_James)
    love_amount_James = love_amount_Susan + 1
    print("<<<<<<<< love_amount_Susan = ",love_amount_Susan,"<<<<<<<<<<<<<<<<<love_amount_James = ", love_amount_James)
    print(f"So, Susan loves James {love_amount_Susan} stars, while James love Susan {love_amount_James} stars.")
    txt = open(filename).read()
    print(txt)


input(prompt)
showlove()
#showlove(23 + 33, 342 - 33)
