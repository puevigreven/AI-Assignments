import nltk
from nltk import bigrams
from nltk import trigrams

def find_n_grams(source, des) :
    """
    Change in .write function while dealing with Train data.
    """
    with open(source, 'r') as myfile:
        text=myfile.read()
    # type(data)

    unigram_file = open(des, "w")
    # bigram_file = open("ABBR_bigram.txt", "w")
    # trigram_file = open("ABBR_trigram.txt", "w")

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
        unigram_file.write("%s %s\n" % (key ,value))
    # unigram_file.close()

    bigrmdic = {}
    for item in sorted(set(bigramToken)):
        bigrmdic[item] = bigramToken.count(item)
    for key, value in sorted(bigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
        print "%s: %s" % (key, value)
        unigram_file.write("%s %s\n" % (key ,value))
    # bigram_file.close()

    trigrmdic = {}
    for item in sorted(set(trigramToken)):
        trigrmdic[item] = trigramToken.count(item)
    for key, value in sorted(trigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
        print "%s: %s" % (key, value)
        unigram_file.write("%s %s\n" % (key ,value))
    unigram_file.close()

# find_n_grams('final_train.txt', 'train-ngram.txt')


# find_n_grams('NUM-Group.txt' , 'NUM_ngram.txt')
# find_n_grams('LOC-Group.txt' , "LOC_ngram.txt")
# find_n_grams('HUM-Group.txt' , "HUM_ngram.txt")
# find_n_grams('ABBR-Group.txt' , "ABBR_ngram.txt")
# find_n_grams('DESC-Group.txt' , "DESC_ngram.txt")
# find_n_grams('ENTY-Group.txt' , "ENTY_ngram.txt")




