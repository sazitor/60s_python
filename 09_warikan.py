total = int(input("合計金額: "))
people = int(input("人数: "))

each = total // people // 100 * 100
rest = total - each * people

print(f"1人 {each} 円（100円単位）")
print(f"幹事は {each + rest} 円")
