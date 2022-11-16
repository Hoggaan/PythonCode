infile = open('file', 'r')
outfile = open('reports.txt', 'w')

Id = int(infile.readline())
Name = infile.readline().rstrip()
Avg = infile.readline()

print(Name, Id, Avg)

infile.close()
outfile.close()

