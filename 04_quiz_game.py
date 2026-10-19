import random

quiz = {"日本一大きい湖は？": "琵琶湖",
        "1週間は何日？": "7",
        "日本の首都は？": "東京"}
qs = list(quiz)
random.shuffle(qs)
score = 0

for q in qs:
    ans = input(q + " ")
    if ans == quiz[q]:
        print("正解！")
        score += 1
    else:
        print("ざんねん… 正解は", quiz[q])

print(f"{score}/{len(qs)}問 正解！")
