gn = '''ccatcgtagt cttaaccata aaccatgccg actagggatt tgcggttgtt cttgtagact
       61 ccgtaagcac cttatgagaa atcaaagtgt ttgggttccg gggggagtat ggtcgcaagg
      121 ctgaaactta aagaaattga cggaagggca ccaccaggag tggagcctgc ggcttaattt
      181 gactcaacac gggaaaactt accaggtcca gacatagtga ggattgacag attgagagct
      241 ctttcttgat tctatgggtg gtggtgcatg gccgttctta gttggtggag tgatttgtct
      301 ggttaattcc gttaacgaac gagacccccg cctgctaaat agtccggtga atgagttttc
      361 attgacctgg tcttcttaga gggactttcg gtgactaacc gaaggaagtt gggggcaata
      421 acaggtctgt gatgccctta gatgatctgg gccgcacgcg cgctacactg atgcattcaa
      481 cgagtctaga accttggccg agaggcctgg gcaatct'''
gn.replace('\n', '')
for f in gn:
	if f.isalpha():
		print(f, end='')