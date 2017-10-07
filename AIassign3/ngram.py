import nltk
from nltk import bigrams
from nltk import trigrams

# text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare
# tempor lacus, quis pellentesque diam tempus vitae. Morbi justo mauris,
# congue sit amet imperdiet ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare
# tempor lacus, quis pellentesque diam"""
# split the texts into tokens
with open('test_final.txt', 'r') as myfile:
    text=myfile.read()
# type(data)

unigram_file = open("test_unigram.txt", "w")
bigram_file = open("test_bigram.txt", "w")
trigram_file = open("test_trigram.txt", "w")

tokens = nltk.word_tokenize(text)
tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
bi_tokens = bigrams(tokens)
tri_tokens = trigrams(tokens)
trigramToken = list(tri_tokens)
bigramToken = list(bi_tokens)


unigrmdic = {}
for item in sorted(set(tokens)):
	unigrmdic[item] = tokens.count(item)
for key, value in sorted(unigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
    print "%s: %s" % (key, value)
    unigram_file.write("%s: %s \n" % (key, value))
unigram_file.close()

bigrmdic = {}
for item in sorted(set(bigramToken)):
	bigrmdic[item] = bigramToken.count(item)
for key, value in sorted(bigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
    print "%s: %s" % (key, value)
    bigram_file.write("%s: %s \n" % (key, value))
bigram_file.close()


    

trigrmdic = {}
for item in sorted(set(trigramToken)):
	trigrmdic[item] = trigramToken.count(item)
for key, value in sorted(trigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
    print "%s: %s" % (key, value)
    trigram_file.write("%s: %s \n" % (key, value))
trigram_file.close()


