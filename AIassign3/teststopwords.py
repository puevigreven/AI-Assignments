import pandas as pd
pos_tweets = [('I love this car', 'positive'),
    ('This view is amazing', 'positive'),
    ('I feel great this morning', 'positive'),
    ('I am so excited about the concert', 'positive'),
    ('He is my best friend', 'positive')]

test = pd.DataFrame(pos_tweets)
test.columns = ["tweet","class"]

from nltk.corpus import stopwords
stop = stopwords.words('english')

test['tweet_without_stopwords'] = test['tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
print(test)
# Out[40]:
