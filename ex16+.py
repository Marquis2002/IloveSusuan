from sys import argv
script, filename = argv

print(f"We're going to read {filename}")
input("Hit Enter to continue")

txt = open(filename)
txt.seek(0)

print(txt.read())
print(txt.readline())
