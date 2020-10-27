from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os
filename= "/mnt/c/Users/usuario/Desktop/ls_orchid.gbk"
def summarize_contents(filename):
	FileList = []
	File_Extension = []
	
	if(File_Extension[1] == ".gbk"):
		type_file= "genbank"
	else:
		type_file= "fasta"
		pass
	
	records = list(SeqIO.parse(filename, type_file))
	cadena = " "
	path= os.path.dirname(filename)
	
	cadena=("File: " + FileList[1])
	cadena+= ("\nPath " + path)
	cadena+= ("\nnum_records= " + str(len(records)))
	
	for seq_record in SeqIO.parse(filename, type_file):
		cadena+= ("\n-ID " + str(seq_record.id))
		cadena+= ("\nName: " + str(seq_record.name))
		cadena+= ("\nDescription " + str(seq_record.description))
	return cadena

	if _name_ == "_main_":
		r = summarize_contents(filename)
		print(r)
