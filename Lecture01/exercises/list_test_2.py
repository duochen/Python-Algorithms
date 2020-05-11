fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]
fruits.extend(vegetables)
print(fruits)
vegetables.append('bean')
print(vegetables)
vegetables.sort()
print(vegetables)
vegetables.sort(reverse=True)
print(vegetables)
print(fruits.count("berries"))
print(fruits.index("grapes"))
fruits.insert(0, "banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.remove("kale")
print(vegetables)
del vegetables
# NameError: name 'vegetables' is not defined
print(vegetables)