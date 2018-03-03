# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:08:14 2017

@author: BHAVIK
"""
from nltk.corpus import stopwords
import re
from nltk import load
from nltk.tokenize import sent_tokenize
import nltk

def loadFile(file):
    con=set()
    fopen=open(file)
    for line in fopen:
        con.add(line.strip())
    fopen.close()
    return con
      

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence
    
    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms


def run(path):
    phrases = loadFile("contextphrase.txt") 
    reviews = loadFile(path)
    fword=open("relevant.txt",'w')
    
    nonrel=set(loadFile('nonrelevant.txt'))
    stopLex=set(stopwords.words('english')) # build a set of english stopwrods 
    
    wordlist=set()
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    POStags=['NN'] # POS tags of interest 
    
    for line in reviews:
        
        line=line.lower().strip().split('.')
       
        for phrase in phrases:
            phrase=phrase.lower().strip()
            for i in range(0,len(line)):
                if phrase in line[i]:
                
                    try:
                       
                        word=line[i].partition(phrase)[2].split(" ")[1]
                        word=re.sub('[^a-z]',' ',word)
                        
                        word = nltk.word_tokenize(word)
                        
                        
                        POSterms=getPOSterms(word,POStags,tagger)
                        word=POSterms['NN']
                        word=''.join(word)
                        
                        if word==' ' or word in stopLex or word in nonrel:continue
                        else: wordlist.add(word)
                        
                    except:
                        continue
    wordlist='\n'.join(wordlist)
    fword.write(str(wordlist)+"\n")
    fword.close()

if __name__=='__main__':
    path='HotelReviews.txt'
    run(path)