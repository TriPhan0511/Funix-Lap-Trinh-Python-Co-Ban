line1 = "This here's the wattle,\n"
fout = open('output2.txt', 'w')
fout.write(line1)

fout.write('This is the second line.\n')
fout.write('This is the third line.\n')

fout.close()