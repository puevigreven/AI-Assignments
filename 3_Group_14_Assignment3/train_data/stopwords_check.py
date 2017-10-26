from nltk.corpus import stopwords

# data = pd.read_csv('train.txt', sep=":")
operators = set(('what', 'who', 'when' , 'where' , 
	'which' , 'why' , 'what\'s' , 'who\'s' , 
	'when\'s' , 'where\'s' , 'how'))

stop = set(stopwords.words('english')) - operators

print list(stop)
# l = []
# for i in stop:
# 	print i