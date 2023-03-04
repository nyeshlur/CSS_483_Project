with open('Yeast_Essential_Genes_Alt.txt', 'r') as istr:
    with open('modified.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + ' E'
            print(line, file=ostr)