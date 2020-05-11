fruits = {"grapes", "apples", "berries"}
animals = (("lion", "tiger", "bear"))
fruits.add("oranges")
print(fruits)
fruits.update(["mango","kiwi"])
print(fruits)
fruits.remove("kiwi")
print(fruits)
fruits.clear()
print(fruits)
print(animals)
del animals
# NameError: name 'animals' is not defined
print(animals)