# use the argv module from sys
from sys import argv
# claim two arguments
script, input_file = argv
# define a print function
def print_all(f):
    # print f to test it
    print("<<<<<< print_all: f = ", f)
    # use read to print
    print(f.read())
    # print f to test it
    print("<<<<<< print_all: f = ", f)
#define a rewind function, like a tape.
def rewind(f):
    # use seek to go back home
    f.seek(0)
#define a print function to print a line.
def print_a_line(line_count, f):
    # use readline to print a line
    print("<<<<<<< line_count = ", line_count)
    print(line_count, f.readline(), end = '')
    print("<<<<<<< line_count = ", line_count)

# open the file to use the function
current_file = open(input_file)
# nothing important, a clue
print("First, let's print the whole file: \n")
# use print_all function
print_all(current_file)
# nothing important, a clue
print("Now let's rewind, kind of like a tape.")
# use rewind function
rewind(current_file)
# nothing important, a clue
print("Now let's print three lines:\n")
# define a order name
current_line = 1
# use print line function
print_a_line(current_line, current_file)
# just plus one
current_line += 1
# print a line again
print_a_line(current_line, current_file)
# like above
current_line += 1
# like above
print_a_line(current_line, current_file)
