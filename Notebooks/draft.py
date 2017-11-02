with open("./data/tweets.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

documents_tokens = [tokenizer.tokenize(d) for d in documents]
print(documents_tokens[0])

from nltk.corpus import stopwords
print(stopwords.words('spanish'))
print(len(documents_tokens))
docs_tokens_filtered = [[w for w in tokens if not w in stopwords.words('spanish')] for tokens in documents_tokens]