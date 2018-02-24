#how many 0??____question1
#q1 = how many 5 and 2, the number of zero = min(2'number, 5'number)
#bingo
list_5 = []
list_2 = []
l = [2, 80, 3, 500]
for x in l:
    i = 0
    j = 0
    while x % 5 == 0:
        x = x/5
        i = i + 1
    list_5.append(i)
    while x % 2 == 0:
        x = x/2
        j = j + 1
    list_2.append(j)
a = sum(list_2)
b = sum(list_5)
c = min(a, b)
print(list_2)
print(list_5)
print(c)











