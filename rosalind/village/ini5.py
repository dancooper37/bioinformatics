data = open("rosalind_ini5.txt", "r")

i = 1
for line in data.readlines():
    if i % 2 == 0:
        print(line)
    i += 1
