import sys

with open(sys.argv[1]) as fin:
    for line in fin:
        tmp = line.split(' ')
        id =   tmp[0]
        acc = tmp[-2]
        if acc.strip() == 'Assigned' or acc.strip() == 'Withdrawn':
            acc = ''
        print id+","+acc
        #id, acc = line.split('\t')
        #print id, acc
