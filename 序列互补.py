import string
a = string.maketrans('ATCG', 'TAGC')
c = 'TACATGGC'
b = c.translate(a)
print(b)

#
a = 'ATCG'
for i, j in enumerate(a):
    print(i, j)

#
def hello(name, index):
    a = 'hello {0}, your index is {1}'.format(name, index)
    return a
print(hello('mmm', 2))

#
f = open('/Users/nanshenshiqianxuesen/Desktop/chrM.fa', 'r')
for line in f:
    g = line.strip()
    print(g)
f.close


