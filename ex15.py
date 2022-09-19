#Use argv function from sys
from sys import argv
#use argv
script, filename = argv
#open file
txt = open(filename, mode ='rb')
#show the file
print(f"Here's your file {filename}:")
#show the file
print(txt.read())
#txt.close()
print(txt.read())

#show the clue
print("Type the filename again:")
#use input to get the filename
file_again = input("> ")
#open the file
txt_again = open(file_again)
#display
print(txt_again.read())
