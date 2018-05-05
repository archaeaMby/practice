# _*_ coding:UTF-8 _*_

# 将FASTQ格式转换为FASTA格式，并另存这个转换的格式
output_file = open(r'/test.fa', 'w')

with open(r'/test.fastq', 'r') as input_fastq:
    for index,line in enumerate(input_fastq):
        if index % 4 == 0:
            output_file.write('>' + line.strip()[1:])  # header
        elif index % 4 == 1:
            for i in range(0, len(line.strip()), 40):   # seq
                output_file.write(line.strip()[i: i+40] + '\n')
        elif index % 4 == 2:
            continue   # annotation
        elif index % 4 == 3:
            continue   # quality

