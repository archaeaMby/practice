L = [2, 8, 3, 50]
print('a')
a = []
for x in L:
    i = 0
    j = 0
    while x % 5 == 0:
        x = x/5
        i = i + 1
    a.append(i)
    while x % 2 == 0:
        x = x/2
        j = j + 1
    a.append(j)
if a[0] >= a[1]:
    print('1')
else:
    print('0')

a = 255
b = []
while a % 2 != 0:
    a = a/2
    b.append(1)
    if a != 1:
        continue
print(len(b))









