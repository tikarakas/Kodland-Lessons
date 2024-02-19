import random
harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
harf = int(input("Şifren kaç harfli olsun?:"))
sifre = ""

for i in range(harf):
    sifre += random.choice(harfler)
print(sifre)
