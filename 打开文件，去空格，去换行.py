f = open('/Users/nanshenshiqianxuesen/Desktop/t.result.txt', 'w')

with open('/Users/nanshenshiqianxuesen/Desktop/t.txt', 'r') as input_f:
    for line in input_f:
        line = line.strip()
        result = int(line) * int(line)
        f.write(str(result) + '\n')

