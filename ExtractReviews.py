# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:08:14 2017

@author: BHAVIK
"""

from bs4 import BeautifulSoup
import requests
import time
import os   #to create folders

def load(path):
    links=set()
    fopen=open(path)
    for line in fopen:
        links.add(line.strip())
    fopen.close()
    return links

def run(url):
    
    pageNum=[10,20,30,40,50]
   
    loadLinks=load('HotelLinks.txt')
    count=0
    for link in loadLinks:
        
        html=None
        hotelname=link.split('/')[2]
        os.makedirs(hotelname, exist_ok=True)
        for p in pageNum:
            #print("Page "+str(p))
                        
            if p==1: pageLink=url+link
            else: pageLink=url+link+'?start='+str(p)
            
            hotelpage = hotelname+"/"+hotelname+"-"+str(p)+".txt"
                   
            fw=open(hotelpage,'w')
            
            frev=open('HotelReviews.txt','a')
            
            for i in range(5):
                try:
                    response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                    html = response.content
                    
                    break;
                except Exception as e:
                    print("failed ",i)
                    time.sleep(2)
        
            if not html:continue;
        
        
            soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml')
            
            fw.write(str(soup))
        
            reviews = soup.findAll('div',{'class':'review review--with-sidebar'})
            
            for review in reviews:
                hotelreview=review.find('p')
                frev.write(hotelreview.text+'\n');
                count = count+1
                
    fw.close()
    frev.close()

if __name__=='__main__':
    url='https://www.yelp.com'
    run(url)
 
