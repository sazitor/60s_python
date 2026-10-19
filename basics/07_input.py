# 1分でわかるPython基礎 #07 input と int

# input: キーボードから入力を受け取る
name = input("名前: ")
print("こんにちは", name)

# input の結果は文字列 → "3" + "4" は "34"
a = input("数: ")
b = input("数: ")
print(a + b)

# int() で数字に変換すれば 3 + 4 = 7
a = int(a)
b = int(b)
print(f"合計は {a + b}")

# よくあるミス: 文字と数字を + でつなぐと TypeError
age = 20
# print("年齢: " + age)   # TypeError
print(f"年齢: {age}")     # f文字列ならOK
