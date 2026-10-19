# 1分でわかるPython基礎 #02 辞書

# 辞書の作り方: { } で囲んで キー: 値
price = {"りんご": 120, "みかん": 80}

# キーを指定して値を取り出す
print(price["りんご"])    # 120

# 新しいキーなら追加、あるキーなら上書き
price["ぶどう"] = 300
price["みかん"] = 100
print(price)              # {'りんご': 120, 'みかん': 100, 'ぶどう': 300}
print(len(price))         # 3

# よくあるミス: ないキーを指定すると KeyError
# print(price["メロン"])  # KeyError: 'メロン'
print("メロン" in price)  # False（in で先に確認できる）
