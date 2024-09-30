# Pythonで特定の文字列以降を削除する
# find()メソッドを使ってみる
s = "123-4567"
pos = s.find("-")
s = s[:pos]
print(s)

# split()メソッドを使ってみる
s = "hogehoge@junkmail.com"
s = s.split("@")[0]
print(s)

# partition()メソッドを使ってみる
s = "hogehoge@junkmail.com"
s = s.partition("@")[0]
print(s)