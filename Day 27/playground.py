# def add(*args):
#     print(sum(args))

# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def calculate(n, **kwargs):
#     sum=n+kwargs["add"]
#     mul=n*kwargs["multiply"]
#     print(sum, mul)

# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kw):
#         self.make=kw.get("make")
#         self.model=kw.get("model")

# my_car=Car(make="Nissan", model="GTR 5")

def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)