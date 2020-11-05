#!/usr/local/bin python3


f = open('input.txt')
f1 = open('output.txt','w')
for x in f.readlines():
    f1.write(x.lower())
f.close()
f1.close()
