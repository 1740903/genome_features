
import pprint as pp
import sys


sys.argv[0]= str(raw_input("File path: "))

def quality():
        
    cnt=0
    quality= dict()
   
        
    with open(sys.argv[0]) as input_file:
        for line in input_file:
            line = line.strip()
            cnt=cnt+1
            if cnt%4==2:
                for position, character in enumerate(line):
                    if position=='N':
                        print('here')
                
    
            if cnt%4==0:
                for position, character in enumerate(line):
                    q=ord(character)-33 
                    if cnt/4==1:
                        quality[position]=0
                    quality[position]=quality[position]+q
        for position in quality:      
            quality[position]=float(quality[position])/(cnt/4)
            print  position , quality[position]
    return



def rowAvrage():
    cnt=0
    stats = dict()
    SA=0
    SC=0
    SG=0
    ST=0

    with open(sys.argv[0]) as input_file:
        for line in input_file:
            line = line.strip()
            cnt=cnt+1
            if cnt%4==2:
                for character in line:
                    if character == 'N':
                        continue
                    elif character=='A':
                        SA=int(SA+1)
                    elif character=='C':
                        SC=int(SC+1)
                    elif character=='G':
                        SG=int(SG+1)
                    elif character=='T':
                        ST=int(ST+1)
            else:
                continue  
    s=SA+SC+SG+ST
    print(SA/float(s),SC/float(s),SG/float(s),ST/float(s)) 
    return




def columAvrage():

    cnt=0
    stats = dict()

    with open(sys.argv[0]) as input_file:
        for line in input_file:
            line = line.strip()
            cnt=cnt+1
            if cnt%4==2:
                for position, character in enumerate(line):
                
                    #feels the dictionary for the first time    
                    if cnt==2:
                        stats[position]={'A':0, 'C':0 , 'G':0 , 'T':0}
                
                    #we do not want consider Ns
                    if character == 'N':
                        continue
                    stats[position][character] += 1
                           
            else:
                continue
    #to reach the value of second dictionary
    for position in stats:
        d=stats[position]
        s=sum(d.values())
        for character in d:
            d[character]=d[character]/float(s)
    pp.pprint(stats)
    return

print ("Quality of each line is : ")
quality()
print("\n")
print("Row Avrage of A, C, G, T in orther are: ")
rowAvrage()
print("\n")
print("Colum Avrage of A, C, G, T in orther are: ")
columAvrage()
print("\n")