import string 

def removePuntuation(source , destination):
	with open(source, 'r') as myfile:
		data=myfile.read()

	s = data.translate(None, string.punctuation)
	# print s

	text_file = open(destination, "w")
	text_file.write(s)
	text_file.close()

removePuntuation('ABBR-Group.txt' , 'ABBR-Group.txt')
removePuntuation('HUM-Group.txt' , 'HUM-Group.txt')
removePuntuation('ENTY-Group.txt' , 'ENTY-Group.txt')
removePuntuation('LOC-Group.txt' , 'LOC-Group.txt')
removePuntuation('NUM-Group.txt' , 'NUM-Group.txt')
removePuntuation('DESC-Group.txt' , 'DESC-Group.txt')
