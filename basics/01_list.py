# 1分でわかるPython基礎 #01 リスト

# リストの作り方: [ ] で囲んで , で区切る
hands = ["グー", "チョキ", "パー"]

# 番号（インデックス）で取り出す。最初は 0 番
print(hands[0])   # グー
print(hands[2])   # パー

# len で中身の数、append で後ろに追加
print(len(hands))         # 3
hands.append("キツネ")
print(len(hands))         # 4

# よくあるミス: 3つのリストで hands[3] を指定すると IndexError
colors = ["赤", "青", "黄"]
print(colors[2])          # 黄（最後は 2 番）
# print(colors[3])        # IndexError: list index out of range
