class Child:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

class Adult:
    def __init__(self, name, age, gender, child):
        self.name = name
        self.age = age
        self.gender = gender
        self.child = child

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_child_name(self):
        return self.child.get_name()

def main():
    zoe = Child("Zoe", 4, "Female")
    missan = Child("Missan", 2, "Female")
    tosan = Child("Tosan", 4, "Female")
    segun = Child("Segun", 3, "Male")
    children = [zoe, missan, tosan, segun]

    for child in children:
        tinuke = Adult("Tinuke", 25, "Female", child)
        print(tinuke.get_child_name())

main()
