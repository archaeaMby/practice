# _*_ coding:UTF-8 _*_

# date 2018/02/25

# 人类线粒体基因组的简单操作

##########################################
chrM = ''
with open('/Users/nanshenshiqianxuesen/Desktop/data/chrM.fa', 'r') as input_file:
    for line in input_file:
        if line[0] != '>':    #判断是否为标题
            line = line.strip().upper()
            chrM = chrM + line

print(len(chrM))
print(chrM.count('A'))
print(chrM.count('C'))
print(chrM.count('G'))
print(chrM.count('T'))

print('the char A in chrM is: {0}'.format(chrM.count('A')))


