import vcf
import sys

nummber=0 

sys.argv[0]= str(raw_input("File path : "))
vcf_reader= vcf.Reader(open(sys.argv[0]))
for record in vcf_reader: 
    print record.CHROM, record.POS, record.ID, record.REF, record.ALT, record.FILTER, record.INFO["AF"] 
        
