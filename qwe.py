import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = 'python/' # Directory of corpus.

newcorpus = PlaintextCorpusReader(corpusdir, '.*')
print(newcorpus.words())