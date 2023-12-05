from collections import namedtuple

person = namedtuple('Person',['fname','lname'])

person1 = person('a','b')

print(person1._asdict())