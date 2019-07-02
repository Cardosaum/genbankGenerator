from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 

with open("example.fasta") as file:

	records = parse(file, "fasta")
	for record in records:    
	   print("Id: {}".format(record.id)) 
	   print("Name: {}".format(record.name))
	   print("Description: {}".format(record.description))
	   print("Annotations: {}".format(record.annotations))
	   print("Sequence Data: {}".format(record.seq))
	   print("Sequence Alphabet: {}".format(record.seq.alphabet))