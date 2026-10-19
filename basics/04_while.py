# 1分でわかるPython基礎 #04 whileループ

# 条件が True の間くり返す
n = 3
while n > 0:
    print(n)
    n -= 1
print("発射！")

# while True と break: 好きなタイミングで抜け出す
while True:
    cmd = input("コマンド（q でおわり）: ")
    if cmd == "q":
        break
print("おわり")

# よくあるミス: n -= 1 を忘れると無限ループ（Ctrl + C で止める）
