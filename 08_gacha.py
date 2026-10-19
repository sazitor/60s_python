import random

items = ["SSR", "SR", "R"]
rates = [1, 19, 80]
n = int(input("何回引く？ "))

result = random.choices(items, rates, k=n)

for item in items:
    print(item, result.count(item), "回")
