# reading files
f1 = open("<path>", "r")
f2 = open("<path>", "r")

print("Appending.........")
for line1 in f1:
    for line2 in f2:
        #Matching lines from line1 and line2
        if line1 != line2:
            f3 = open("<path>","a")
            # f3.write("\n")
            f3.write(line2)
            f3.close()
        else:
            break
f1.close()
f2.close()
print("Appended")
print("Sorting.........")
bands = list()

#read bands from file
filename = 'Output.txt'
with open(filename) as fin:
    for line in fin:
        bands.append(line.strip())

#sort bands
bands.sort()
print(bands)

#write sorted bands
filename = 'Sorted.txt'
with open(filename, 'w') as fout:
    for band in bands:
        fout.write(band + '\n')
