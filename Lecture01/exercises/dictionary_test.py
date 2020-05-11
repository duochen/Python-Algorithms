car = {
    "brand": "BMW",
    "model": "X5",
    "year": "2019"
}
print(car)

greens = dict(fruits="apples", vegetables="kale")
print(greens)
print(car.get("year"))
print(car.update({"color":"silver"}))
print(car)
print(car.keys())
print(car.values)
car.pop("model")
print(car)
car.clear()
print(car)
del car
# NameError: name 'car' is not defined
print(car)