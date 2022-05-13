from string import ascii_lowercase

dic = {}
dic.update(zip(ascii_lowercase[:10], range(1, 11)))
dic.update(zip(ascii_lowercase[10:19], range(20, 101, 10)))
dic.update(zip(ascii_lowercase[19:], range(200, 1001, 100)))

name = input("name: ")
acc = 0
for c in name.lower():
    try:
        acc += dic[c]
    except KeyError:
        pass

print(f"Seu número é {acc}")
