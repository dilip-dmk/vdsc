import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import word_tokenize
import re


corpusdir = 'python/' # Directory of corpus.

newcorpus = PlaintextCorpusReader(corpusdir, '.*')
print(newcorpus.fileids()[0])
print(type(newcorpus))
#print newcorpus.raw()
print newcorpus.words(newcorpus.fileids()[0])
print(len(newcorpus.words()))

tokens = word_tokenize(newcorpus.raw())
#type(tokens)
print len(tokens)
print tokens[:50]
#tokens[:10]
print newcorpus.sents()
print

#to remove comments
def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string fdf
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    return string

print(removeComments(newcorpus.words(newcorpus.raw())))