m = int(input("一つ目の数字:"))
n = int(input("二つ目の数字:"))

if n > m:
    tmp = m
    m = n
    n = tmp


d = m % n
while not d == 0:
    m = n
    n = d
    d = m % n


print(f"二つの数字の最大公約数は「{n}」です。")