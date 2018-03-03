# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:08:14 2017

@author: BHAVIK
"""

def load(file):
    con=set()
    fopen=open(file)
    for line in fopen:
        con.add(line.strip())
    fopen.close()
    
    return con
      

def run(path):
    getContext = load("contextwords.txt")
  
    fcont=open("contextphrase.txt",'w')
    fin=open(path)
    phrase=set()
    for line in fin:
        i=0
        line=line.lower().strip()
        
        words = line.split(' ')
            
        for word in words:
            i=i+1
            if word in getContext and i>6:
                try:
                    phrase=str(words[i-4]+" "+words[i-3]+" "+words[i-2])
                    fcont.write(phrase+'\n')
                                     
                    
                except:
                    continue
            
    fin.close()
    fcont.close()

if __name__=='__main__':
    path='HotelReviewsN.txt'
    run(path)