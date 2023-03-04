f = open('networkdata.txt','r')
a = ['4932.']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('networkdata.txt','w')
for line in lst:
    f.write(line)
f.close()