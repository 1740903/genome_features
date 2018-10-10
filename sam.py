import pprint as pp
import sys

total=0
mapped=0
unmapped=0
secondary=0
ppaired=0

sys.argv[0]= str(raw_input("File path : "))
with open(sys.argv[0]) as myfile:
    for line in myfile:
        line = line.strip().split()

        l = int(line[1])
        b = bin(l)[2:]
        flag=(b.zfill(12))

        total+=1

        if (flag)[9]=='0':
            mapped+=1

        if (flag)[9]=='1':
            unmapped+=1

        if (flag)[3]=='1':
            secondary+=1

        if (flag)[3]=='0':
            ppaired+=1


print ('Total: ',total)

print ('mapped reads : ',mapped)

print ('unmapped reads : ',unmapped)

print ('secondary : ',secondary)

print ('paired in sequencing : ',ppaired)

