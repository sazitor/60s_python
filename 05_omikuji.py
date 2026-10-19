import random

input("Enterでおみくじを引く")
n = random.randint(1, 100)

if n <= 10:
    result = "大吉"
elif n <= 40:
    result = "中吉"
elif n <= 80:
    result = "小吉"
else:
    result = "凶"

print(f"結果は… {result}！")
