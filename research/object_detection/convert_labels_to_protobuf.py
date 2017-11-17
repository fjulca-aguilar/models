tmp_text = "item {\nname: \"%s\"\nid: %d\ndisplay_name: \"%s\"\n}\n"

def convert(input_file, output_file):
	label_id = 1
	with open(input_file, 'r') as fin:
		with open(output_file, 'w') as fout:
			for label in fin.readlines():
				label = label.strip()
				fout.write(tmp_text % (label, label_id, label))
				label_id += 1

convert("../../../../../Documentos/doutorado/program/resources/system_configuration/parameters/crohme/listSymbolCrohme2013noJunk.txt", 
	'data/math_label_map.pbtxt')


