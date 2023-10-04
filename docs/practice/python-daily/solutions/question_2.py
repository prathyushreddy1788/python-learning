def oldest_person(people):
    oldest_person = []
    oldest_age = 0
    for name, age in people.items():
        if age > oldest_age:
            oldest_person = []
            oldest_person.append(name)
            oldest_age = age
        elif age == oldest_age:
            oldest_person.append(name)
    return oldest_person

people = {"Alice": 30, "Bob": 40, "Charlie": 35, "David": 40}
print(oldest_person(people))

