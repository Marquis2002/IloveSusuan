# class Parent(object):
#     def implicate(self):
#         print("PARENT implicate()")


# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()

# dad.implicate()
# son.implicate()

# method 2
# class Parent(object):

#     def override(self):
#         print("PARENT overrride()")


# class Child(Parent):

#     def override(self):
#         print("CHILD override()")

# class GrandChild(Child):
    
#     def override(self):
#         return super().override()


# dad = Parent()
# son = Child()

# dad.override()
# son.override()

# method 3

# class Parent(object):
#     def altered(self):
#         print("PARENT altered()")

# class Child(Parent):
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()


class Parent(object):
    def __init__(self):
        print("PARENT __init__()")
    def implicate(self):
        print("PARENT implicate()")
    def override(self):
        print("PARENT override()")
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def __init__(self, stuff):
        print("CHILD __init__()")
        self.stuff = stuff
        super(Child, self).__init__()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child("23423")


dad.implicate()
son.implicate()

dad.override()
son.override()

dad.altered()
son.altered()


