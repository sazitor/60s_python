import random, time

words = ["python", "print", "while",
         "import", "random"]
random.shuffle(words)
score = 0

start = time.time()
for w in words:
    ans = input(f"{w}: ")
    if ans == w:
        score += 1
end = time.time()

print(f"{score}/{len(words)}問 正解")
print(f"タイム: {end - start:.1f}秒")
