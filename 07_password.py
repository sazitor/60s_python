import secrets
import string

chars = string.ascii_letters
chars += string.digits + "!#$%&"
n = int(input("長さ: "))

pw = ""
for i in range(n):
    pw += secrets.choice(chars)

print("パスワード:", pw)
