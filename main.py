import subprocess


myformat= str(raw_input("Please give the file format : "))
if myformat in ["fastq", "Fastq", "FASTQ", "FastQ"]:
    import fastq
elif myformat in ["sam","SAM","Sam"]:
    import sam
elif myformat in ["bam","BAM", "Bam"]:
    subprocess.call('samtools -S CP1-L007.bam > CP1-L007.sam', shell=True)
    import sam
elif myformat in ["vcf","VCF","Vcf"]:
    import VCF_data
else:
    print("Sorry! it is not a kind of format that I know")