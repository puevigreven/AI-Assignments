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
    stopwords = ['all', 'just', 'being', 'over', 'through', 'yourselves', 'its', 'before', 'hadn', 'with', 'll', 'had', 'should', 'to', 'only', 'won', 'under', 'ours', 'has', 'wouldn', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'd', 'did', 'didn', 'these', 't', 'each', 'because', 'doing', 'theirs', 'some', 'hasn', 'are', 'our', 'ourselves', 'out', 'for', 'weren', 're', 'does', 'above', 'between', 'mustn', 'she', 'be', 'we', 'here', 'shouldn', 'hers', 'by', 'on', 'about', 'couldn', 'of', 'against', 's', 'isn', 'or', 'own', 'into', 'yourself', 'down', 'mightn', 'wasn', 'your', 'from', 'her', 'whom', 'aren', 'there', 'been', 'few', 'too', 'then', 'themselves', 'was', 'until', 'more', 'himself', 'both', 'but', 'off', 'herself', 'than', 'those', 'he', 'me', 'myself', 'ma', 'this', 'up', 'will', 'while', 'ain', 'below', 'can', 'were', 'my', 'at', 'and', 've', 'do', 'is', 'in', 'am', 'it', 'doesn', 'an', 'as', 'itself', 'o', 'have', 'further', 'their', 'if', 'again', 'no', 'that', 'same', 'any', 'other', 'yo', 'shan', 'needn', 'haven', 'after', 'most', 'such', 'a', 'don', 'i', 'm', 'having', 'so', 'y', 'the', 'yours', 'once']
    unigram_file = open(des, "w")
    # count_file = open("total_words_in_classes.txt", "a")

    # bigram_file = open("ABBR_bigram.txt", "w")
    # trigram_file = open("ABBR_trigram.txt", "w")

    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
    bi_tokens = bigrams(tokens)
    tri_tokens = trigrams(tokens)
    trigramToken = list(tri_tokens)
    bigramToken = list(bi_tokens)

    total_count = 0
    uni_count = 500
    uc = 0
    unigrmdic = {}
    for item in sorted(set(tokens)):
        unigrmdic[item] = tokens.count(item)
    for key, value in sorted(unigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
        total_count = total_count + value
        if key not in stopwords and uc < uni_count:
            print "%s: %s" % (key, value)
            unigram_file.write("%s : %s\n" % (key ,value))
            uc = uc + 1
    # unigram_file.close()

    bc = 0
    bigrmdic = {}
    for item in sorted(set(bigramToken)):
        bigrmdic[item] = bigramToken.count(item)
    for key, value in sorted(bigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
        if bc < 300:
            print "%s: %s" % (key, value)
            total_count = total_count + value
            unigram_file.write("%s : %s\n" % (key ,value))
            bc = bc + 1
    # bigram_file.close()
    tc = 0
    trigrmdic = {}
    for item in sorted(set(trigramToken)):
        trigrmdic[item] = trigramToken.count(item)
    for key, value in sorted(trigrmdic.iteritems(), key=lambda (k,v): (v,k) ,reverse=True):
        if tc < 200:
            print "%s: %s" % (key, value)
            total_count = total_count + value
            unigram_file.write("%s : %s\n" % (key ,value))
            tc = tc + 1
    
    # count_file.write("%s : %s" % (source , str(total_count)))
    # count_file.close()
    unigram_file.close()

find_n_grams('final_train.txt', 'train-ngram.txt')


# find_n_grams('NUM-Group.txt' , 'NUM_ngram.txt')
# find_n_grams('LOC-Group.txt' , "LOC_ngram.txt")
# find_n_grams('HUM-Group.txt' , "HUM_ngram.txt")
# find_n_grams('ABBR-Group.txt' , "ABBR_ngram.txt")
# find_n_grams('DESC-Group.txt' , "DESC_ngram.txt")
# find_n_grams('ENTY-Group.txt' , "ENTY_ngram.txt")




