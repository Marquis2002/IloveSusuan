class Other(object):
    def override(self):
        print("OTHER override()")

    def implicate(self):
        print("OTHER implicate()")

    def altered(self):
        print("OTHER altered()")


class Child(object):
    def __init__(self):
        self.other = Other()
    def implicate(self):
        self.other.implicate()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicate()
son.override()
son.altered()
