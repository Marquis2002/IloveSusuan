# use sys module
import sys
# define three arguments
script, encoding, error = sys.argv

# define main function to print every line in a specific method
def main(language_file, encoding, errors):
    print(">>>> main:", repr(language_file), encoding, errors)
    # get a line
    line = language_file.readline()
    # recursion definition
    if line:
        print(">> there's a line: ", repr(line))
        # use print_line function
        print_line(line, encoding, errors)
        print("<< calling main again")
        # recursion definition
        return main(language_file, encoding, errors)
    print("<<<<exit main")

# define the print_line function:
def print_line(line, encoding, errors):
    # DBES: decode bytes, encode strings
    # del the space at the end of lines, we konw readline will add sapce
    next_lang = line.strip()
    # don't know encode(), maybe show the unicode
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # don't know decode(), maybe show the content
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    # print the Unicode and the content
    print(raw_bytes,"<===>",cooked_string)

# well, open the file, like putting a tape into the machine
languages = open("languages.txt", encoding = "utf-8")
# call the main function
main(languages, encoding, error)
