# ten lists' application
# Susan is a pig.
susan_pig = ['Susan', 'is', 'a', 'pig']
print(susan_pig)
print(len(susan_pig))
susan_is_a_pig = ' '.join(susan_pig)
susan_pig_again = susan_is_a_pig.split(' ')
print("Join susan pig is", susan_is_a_pig)
print("split it again", susan_pig_again)

print("Now we could append something new to it.")
susan_pig_again.append(",big pig.")
print(susan_pig_again)

print(' '.join(susan_pig_again))

# list[]
#
# for i in range(0,5):
#     a = susan_pig_again.pop(0)
#     print(a)
#     print(susan_pig_again)
#     while len(susan_pig) != 10
#     print(susan)
