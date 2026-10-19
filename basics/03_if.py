# 1分でわかるPython基礎 #03 if文

# if: 条件が True のときだけ実行
age = 15
if age < 20:
    print("学生料金")

# elif: 3つ以上に分ける（上から順にチェックして、最初の1つだけ実行）
if age < 13:
    print("子ども 500円")
elif age < 20:
    print("学生 800円")     # ← age = 15 ならここ
else:
    print("大人 1200円")

# よくあるミス: 比べるときは = ではなく ==
# if age = 15:            # SyntaxError
if age == 15:
    print("15歳")
