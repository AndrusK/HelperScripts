import sys
from itertools import zip_longest

if len(sys.argv) < 3:
	print("split_large_file.py [input file] [lines per file]")

in_file = sys.argv[1]
lines = sys.argv[2]

smallfile = None
with open(in_file) as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % int(lines) == 0:
            if smallfile:
                smallfile.close()
            small_filename = '{0}_{1}.txt'.format(in_file, int(lineno) + int(lines))
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()
