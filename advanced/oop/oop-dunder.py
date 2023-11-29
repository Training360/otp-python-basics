class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # human readable representation
    def __str__(self):
        return f'firstname: {self.first_name}, lastname: {self.last_name}'

    # like str, just for machines
    def __repr__(self):
        return f'{self.__class__.__name__} ({self.first_name}, {self.last_name})'

    def __eq__(self, other):
        if self is other:
            return True
        elif not isinstance(other, Person):
            return False
        else:
            # TODO: check attributes length too
            return self.first_name == other.first_name and self.last_name == other.last_name


p1 = Person('John', 'Doe')
p2 = Person('John', 'Doe')

print(p1)
print(repr(p1))

print(p1 == p2)
