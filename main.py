import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
colvo= int(input('длинна пороля'))
passwd= ''
for i in range(colvo):
    b = a[random.randint(0,len(a)-1)]
    passwd += b
print(passwd)