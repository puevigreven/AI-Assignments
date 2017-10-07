import pandas as pd
from nltk.corpus import stopwords

# data = pd.read_csv('train.txt', sep=":")
operators = set(('what', 'who', 'when' , 'where' , 
	'which' , 'why' , 'what\'s' , 'who\'s' , 
	'when\'s' , 'where\'s'))

stop = set(stopwords.words('english')) - operators

df = pd.read_table('train.txt', delimiter=':', names=('A', 'B', 'C'))

df["C"] = df["C"].str.lower().str.split()
# test['tweet'].apply(lambda x: [item for item in x if item not in stop])

df['C'].apply(lambda x: [item for item in x if item not in stop])
# test['tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

df.to_csv("refined_train.csv", encoding='utf-8')



# from nltk import word_tokenize
# import nltk
# import io
# # nltk.download('stopwords')

# stop = set(stopwords.words('english')) - operators

# # for p in stop:
# # 	print p


# #word_tokenize accepts a string as an input, not a file.
# file1 = open("train.txt")
# i = 0
# line = file1.read()# Use this to read file content as a stream:
# words = line.split()
# for r in words:
# 	appendFile = open('filteredtext.txt','a')
# 	if (r == '?'):
# 		i+=1
# 		print i
# 		appendFile.write('\n')
# 		appendFile.close()
# 		continue
# 	if not r in stop:
# 		appendFile.write(" "+r)
# 		appendFile.close()
