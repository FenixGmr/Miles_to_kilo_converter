def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,6,7,8,9))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)