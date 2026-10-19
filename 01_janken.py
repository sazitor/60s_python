import random

hands = ["グー", "チョキ", "パー"]
win = {"グー": "チョキ",
       "チョキ": "パー",
       "パー": "グー"}

me = input("あなたの手: ")
cpu = random.choice(hands)
print("CPU:", cpu)

if me == cpu:
    print("あいこ！")
elif win[me] == cpu:
    print("あなたの勝ち！")
else:
    print("あなたの負け…")
