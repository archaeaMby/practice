# _*_ coding:UTF-8 _*_

# 把fasta格式转化为fastq格式

# with open(r'/Users/nanshenshiqianxuesen/Desktop/data/chrM.fa', 'r') as input_file:
#     seq = ''
#     header = input_file.readline().strip()[1:]
#     for line in input_file:
#         line = line.strip()
#         if line[0] != '>':
#             seq = seq + line
#         else:
#             print(seq)
#             print(header)
#             seq = ''
#             header = line[1:]


# 序列互补的改进版本
import string
def com_rev(input_seq):
    translate_table = string.maketrans('ATCG', 'TAGC')
    return input_seq.upper().translate(translate_table)[::-1]

print(com_rev('agggtc'))



