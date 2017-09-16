
import sys

with open(sys.argv[1]) as csv:
    print csv.next().strip()
    for line in csv:
        splitted = line.strip().split('"')
        splitted[-2] = '{' + splitted[-2][:-1] + '}'
        print '"'.join(splitted)

