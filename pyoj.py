#output dict's keys and arrange these
#bingo
a = {1: 1, 2: 2, 3: 3}
b = map(str, a.keys())
new_a = ','.join(sorted(b))
print(new_a)
print(type(a.keys()))

#filter prime in 0,100.
#bingo
r = [2]
for i in range(3, 100):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        r.append(i)
prime = ' '.join(map(str, r))
print(prime)

#print string who are in the odd site
#bingo
a_2 = 'xyzwd'
b_2 = []
for i in range(0, len(a_2), 2):
    b_2.append(a_2[i])
c_2 = map(str, b_2)
print(''.join(c_2))



