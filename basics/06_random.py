# 1分でわかるPython基礎 #06 random

import random   # 忘れると NameError

# choice: リストからランダムに1つ選ぶ
hands = ["グー", "チョキ", "パー"]
print(random.choice(hands))

# randint: 範囲の整数をランダムに（終わりの 6 も含む）
print(random.randint(1, 6))

# shuffle: リストの順番をバラバラにする
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)
