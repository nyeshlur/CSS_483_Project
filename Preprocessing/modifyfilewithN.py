with open('Yeast_NonEssential_Genes_Alt.txt', 'r') as istr:
    with open('modified2.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + ' N'
            print(line, file=ostr)