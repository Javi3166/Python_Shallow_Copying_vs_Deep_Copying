"""
- shallow copy: one level deep, only references of nested child objects
- deep copy: full independent copy
"""

import copy

print("Example 1")
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)

print("\nExample 2")
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
'''
All work for lists too
cpy = org.copy()
cpy = list(org)
cpy = org[:]
'''
cpy[0] = -10
print(cpy)
print(org)

print("\nExample 3")
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)

print("\nExample 4")
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

print("\nExample 4")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 27)
p2 = p1

p2.age = 28
print(p1.age)
print(p2.age)

print("\nExample 5")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 27)
p2 = copy.copy(p1)

p2.age = 28
print(p1.age)
print(p2.age)

print("\nExample 6")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 42
print(company.boss.age)
print(company_clone.boss.age)

print("\nExample 7")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 42
print(company.boss.age)
print(company_clone.boss.age)