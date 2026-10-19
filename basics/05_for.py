# 1分でわかるPython基礎 #05 forループ

# range(5) は 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# リストの中身を1つずつ取り出す
hands = ["グー", "チョキ", "パー"]
for h in hands:
    print(h)

# range(始め, 終わり): 終わりの数は含まない → 1〜5
for i in range(1, 6):
    print(i)

# よくあるミス: 中の処理をインデントし忘れると IndentationError
