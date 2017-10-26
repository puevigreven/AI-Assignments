import nltk
from nltk import bigrams
from nltk import trigrams
import pandas as pd

dest = "final_output.txt"
unigram_file = open(dest, "w")

check_file = "test_final.txt"
with open(check_file) as f:
	    cf = f.readlines()
test = [x.strip() for x in cf]
g = 0
for text in test:
	# text = "Who was Galileo"
	print g
	g = g +1
	tokens = nltk.word_tokenize(text)
	tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
	bi_tokens = bigrams(tokens)
	tri_tokens = trigrams(tokens)

	m = ["HUM_probability.txt","ENTY_probability.txt","NUM_probability.txt","LOC_probability.txt","ABBR_probability.txt","DESC_probability.txt"]

	tok = [tokens, bi_tokens, tri_tokens]
	# check_file = "HUM_probability.txt"

	l = []
	l.extend(tokens)
	l.extend(bi_tokens)
	l.extend(tri_tokens)
	# tokens.extend(list(tri_tokens))
	# tokens.extend(list(bi_tokens))
	# tokens.extend(list(tri_tokens))
	max_str = ""
	max_val = -1
	for e in m:
		with open(e) as f:
			cf = f.readlines()
		cf = [x.strip() for x in cf]
		s = 0
		
		product = 1.0
		for k in l:
			# print k
			for t in cf:
				if str(k) in t:
					product = product * float(t.split(" : ")[1] )
					# print (product)
					break

		if max_val < product:
			max_val = product
			max_str = e
		product = 1.0
	unigram_file.write("%s : %s\n" % (text ,max_str.split("_")[0]))
unigram_file.close()
	# print max_str.split("_")[0]


