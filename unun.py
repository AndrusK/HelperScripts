import sys

if len(sys.argv) < 3:
    print("unun.py [infile] [outfile]")

new_file = []
file = open(sys.argv[1])

for line in file:
    new_file.append(line.strip()+":"+line)

output_file = open(sys.argv[2],'w')
for element in new_file:
    output_file.write(element)

output_file.close()
