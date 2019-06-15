# Generating a Genbank File using Biopython
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqFeature import SeqFeature, FeatureLocation

sequences = ["GGGGAAAATTTTAAAACCCCAAAA","AAAATTTTAAAACCCCAAAAGGGG"]

listOfseqrecords = []

for sequence in sequences:
	seq = Seq(sequence, IUPAC.unambiguous_dna) # unambiguous_dna = only ACGT
	seqRecord = SeqRecord( 
		seq, 
		id='123', # sequence ID
		name='EXAMPLE', # Unique name (no blank spaces)
		description='Annotation for the sequence', # anotacao da enzima
		annotations= {"molecule_type":"cDNA", "date":"25-MAR-2019"}
		)
	qualifiers = {
		"EC_number":"9.9.9.9", # enzyme EC
		"info":"value" # other data
	}
	feature = SeqFeature( 
		FeatureLocation( start=0, end=len(sequence) ), 
		type='cDNA', 
		location_operator='', 
		strand=0, id=None, 
		qualifiers=qualifiers, 
		sub_features=None, 
		ref=None, 
		ref_db=None
	) 
	seqRecord.features.append(feature)
	listOfseqrecords.append(seqRecord)

 	#Open the output file to write
	outputFile = open('example.gb', 'w')
	for seqRecord in listOfseqrecords:
		SeqIO.write(seqRecord, outputFile, 'genbank')