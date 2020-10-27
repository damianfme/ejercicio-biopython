#creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = os.path.abspath("data/opuntia.fasta")

#Creacion de funcion
def summarize_contents(filename):
	File_List = []
	File_Extension = []
	
	File_List = os.path.split(filename)
	File_Extension = os.path.splitext(filename)
	
	if(File_Extension[1] == ".gbk"):
		type_file= "genbank"
	else:
		type_file= "fasta"
		
	record = list(SeqIO.parse(filename, type_file))
	#Diccionario
	d = {}
	d['File:'] = File_List[1]
	d['Path:'] = File_List[0]
	d['Num_Records:'] = len(record)
	
	d['Names:'] = []
	d['IDs:'] = []
	d['Descriptions:'] = []
	#Registro de Records
	for seq_rcd in SeqIO.parse(filename, type_file):
		d['Names:'].append(seq_rcd.name)
		d['IDs:'].append(seq_rcd.id)
		d['Descriptions:'].append(seq_rcd.description)
	return d

if __name__ == "__main__":
	resultados = summarize_contents(filename)
	print(resultados)
	
