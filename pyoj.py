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

#the square's length and area
#bingo
a = 3
b = 8
the_area = a * b
the_length = 2 * (a + b)
c = [the_area, the_length]
d = map(str, c)
print(' '.join(d))

#print middle number
#bingo
L = [0, 1, 2, 3, 4]
L_sort = sorted(L)
if len(L_sort) % 2 != 0:
    a = ((len(L_sort)-1) / 2)
    mid_number = L_sort[a]
    flag=1
else:
    flag=0
    a = (len(L_sort)/2)
    b = ((len(L_sort)/2) - 1)
    mid_number =(L_sort[a] + L_sort[b]) / 2.0
    if type(mid_number) == float:
        mid_number = float(mid_number)
    else:
        mid_number = int()
print(mid_number)

#GCD
#bingo
r = []
def gcd(a, b):
    c = min(a, b)
    d = max(a, b)
    for i in range(1, c+1):
        if c % i == 0:
            if d % i == 0:
                r.append(i)
    gcd_r = max(r)
    print(gcd_r)
gcd(3, 5)

#LCM 最小公倍数
#bingo
r = []
def lcm(a, b):
    c = min(a, b)
    d = max(a, b)
    for i in range(1, c+1):
        if c % i == 0:
            if d % i == 0:
                r.append(i)
    gcd_r = max(r)
    print((a*b)/gcd_r)
lcm(33, 5)













