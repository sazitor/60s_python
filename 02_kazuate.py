import random

answer = random.randint(1, 100)
count = 0

while True:
    guess = int(input("1〜100の数: "))
    count += 1
    if guess < answer:
        print("もっと大きい")
    elif guess > answer:
        print("もっと小さい")
    else:
        print(f"正解！{count}回で当たり")
        break
