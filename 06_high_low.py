import random

card = random.randint(1, 13)
win = 0

while True:
    guess = input(f"{card} の次は high/low？ ")
    new = random.randint(1, 13)
    print("次のカード:", new)
    if new > card and guess == "high":
        win += 1
    elif new < card and guess == "low":
        win += 1
    else:
        break
    card = new

print(f"{win}連勝！")
