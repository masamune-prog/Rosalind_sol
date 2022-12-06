import sys
from Bio import SeqIO
from os import remove

if __name__ == "__main__":
    '''
    Given: A quality threshold, along with FASTQ entries for multiple reads.
    Return: The number of reads whose average quality is below the threshold.
    '''
    #input_lines = sys.stdin.read().splitlines()
    f = open('test.txt', 'r+')
    lines = f.readlines()
    threshold = lines[0]
    f.seek(0)
    f.truncate()
    f.writelines(lines[1:])
    count = 0
    print(threshold)
    for record in SeqIO.parse("test.txt", "fastq"):
        qual_list = record.letter_annotations["phred_quality"]
        if sum(qual_list) / len(qual_list) < float(threshold):
            count += 1
    print(count)

    #remove("tmp.fastq")
