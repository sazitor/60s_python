# 60秒で作ってみた ＆ 1分でわかるPython基礎

YouTube Shorts シリーズ「60秒で作ってみた」と「1分でわかるPython基礎」で使ったPythonコードの置き場です。
どのコードもコピペですぐ動きます。

## 動かし方

1. 遊びたいファイルをダウンロード（またはコピーして同じ名前で保存）
2. ターミナルで実行

```
python 01_janken.py
```

Python 3 が入っていれば、追加のインストールは不要です。

## 60秒で作ってみた

| # | 作ったもの | ファイル | 行数 | 学べること |
|---|---|---|---|---|
| 01 | じゃんけんゲーム | [01_janken.py](01_janken.py) | 14行 | リスト / 辞書 / input / random / if・elif・else |
| 02 | 数当てゲーム | [02_kazuate.py](02_kazuate.py) | 13行 | random.randint / while ループ / int() / break |
| 03 | タイピングゲーム | [03_typing_game.py](03_typing_game.py) | 13行 | time.time() / for ループ / random.shuffle / f文字列 |
| 04 | クイズゲーム | [04_quiz_game.py](04_quiz_game.py) | 15行 | 辞書 / list() / for ループ / random.shuffle |
| 05 | おみくじ | [05_omikuji.py](05_omikuji.py) | 12行 | random.randint / if・elif・else / 比較演算子 |
| 06 | ハイ＆ロー | [06_high_low.py](06_high_low.py) | 15行 | while True / break / and / elif |
| 07 | パスワード生成器 | [07_password.py](07_password.py) | 9行 | for ループ / range() / secrets.choice |
| 08 | ガチャ | [08_gacha.py](08_gacha.py) | 7行 | random.choices / リスト / count() |
| 09 | 割り勘計算機 | [09_warikan.py](09_warikan.py) | 6行 | input() / int() / // / f文字列 |

## 1分でわかるPython基礎

作品で使った知識を1つずつ解説するシリーズです。

| # | テーマ | ファイル | 使っている作品 |
|---|---|---|---|
| 01 | リスト | [basics/01_list.py](basics/01_list.py) | #01 じゃんけん / #03 タイピング |
| 02 | 辞書 | [basics/02_dict.py](basics/02_dict.py) | #01 じゃんけん / #04 クイズ |
| 03 | if文 | [basics/03_if.py](basics/03_if.py) | #01 じゃんけん / #05 おみくじ |
| 04 | whileループ | [basics/04_while.py](basics/04_while.py) | #02 数当て / #06 ハイ＆ロー |
| 05 | forループ | [basics/05_for.py](basics/05_for.py) | #04 クイズ / #07 パスワード |
| 06 | random | [basics/06_random.py](basics/06_random.py) | #05 おみくじ / #08 ガチャ |
| 07 | inputとint | [basics/07_input.py](basics/07_input.py) | #02 数当て / #09 割り勘 |

## 改造してみよう

- **じゃんけん**：3回勝負にして、勝った回数を数えてみる
- **数当て**：答えの範囲を1〜1000に広げたり、10回以内に当てられなかったら負けにしてみる
- **タイピング**：単語を増やしたり、間違えた単語を最後に表示してみる
- **クイズ**：自分で問題を追加したり、全問正解でメッセージを出してみる
- **おみくじ**：「末吉」を追加したり、確率を変えてみる
- **ハイ＆ロー**：最高記録を表示してみる
- **パスワード生成器**：記号なしバージョンを選べるようにしてみる
- **ガチャ**：天井（100回で確定）を付けてみる
- **割り勘計算機**：10円単位や500円単位を選べるようにしてみる

次に作ってほしいものは、動画のコメント欄で募集中です。
