import re

ENTY_Group = 33291
NUM_Group = 23682
LOC_Group = 21210
HUM_Group = 33441
ABBR_Group = 1671
DESC_Group = 24714

fname = "train-ngram.txt"
with open(fname) as f:
	content = f.readlines()
content = [x.strip() for x in content]

def train(file_ , val, content, dest):
	unigram_file = open(dest, "w")

	check_file = file_
	with open(check_file) as f:
	    cf = f.readlines()
	cf = [x.strip() for x in cf]
	wrd = [x.strip().split(" : ")[0] for x in cf]
	l = 0
	overall_list = []
	# unigram_file.write("A,B\n")
	for i in content:
		for t in cf:
			test = False
			if i in t:
				p = (int(t.split(" : ")[1] ) + 1.0) / (val + 1000)
				# print t.split(" : ")[0] + " : " + str(t.split(" : ")[1])
				unigram_file.write("%s : %f\n" % (t.split(" : ")[0] ,(p)))
				overall_list.append(t.split(" : ")[0])
				l = l + 1
				test = True
				break
		if test is False:
			p = 1.0 / (val + 1000)
	 		unigram_file.write("%s : %f\n" % (i ,(p)))

	# print len(overall_list)
	o = 0

	# for k in wrd :
	# 	if (k not in overall_list):
	# 		o = o + 1
	# 		p = 1.0 / (val + 1000)
	# 		unigram_file.write("%s : %s\n" % (k ,str(p)))
	unigram_file.close()
	# print str(o) 
	# print len(wrd) - o

train("HUM_ngram.txt", HUM_Group, content, "HUM_probability.txt")
train("ENTY_ngram.txt", ENTY_Group, content, "ENTY_probability.txt")
train("NUM_ngram.txt", NUM_Group, content, "NUM_probability.txt")
train("LOC_ngram.txt", LOC_Group, content, "LOC_probability.txt")
train("ABBR_ngram.txt", ABBR_Group, content, "ABBR_probability.txt")
train("DESC_ngram.txt", DESC_Group, content, "DESC_probability.txt")

