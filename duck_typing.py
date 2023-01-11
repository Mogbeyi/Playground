class Duck:
    def swim_fly(self):
        print("I am a duck and I can swim and fly")

class Goose:
    def swim_fly(self):
        print("I am a goose and I can swim and fly")

class Hippo:
    def walk(self):
        print("I am a Hippo, and I can swim but can't fly")

for obj in Duck(), Goose(), Hippo():
    obj.swim_fly()
