import sys


if len(sys.argv) < 3:
    print("remove_email.py [infile] [outfile]")



new_file = []
file = open(sys.argv[1])

for line in file:
    new_user = line.split('@')[0]
    new_pass = line.split(':')[1].strip()
    new_combo = new_user + ':' + new_pass
    if "_" in new_user:
        continue
    if "-" in new_user:
        continue
    if "." in new_user:
        continue
    else:
        new_file.append(new_combo)
    

    #new_file.append(line.split('@')[0]+":"+line.split(':')[1])
output_file = open(sys.argv[2],'w')
for element in new_file:
    output_file.write(element + "\n")

output_file.close()
