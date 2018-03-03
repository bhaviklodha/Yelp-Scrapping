# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:08:14 2017

@author: BHAVIK
"""

from bs4 import BeautifulSoup
import time
import requests

def run(url):
    
    pageNum=[10,20,30]
    #pageNum=[160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
    cuisine='&cflt=newamerican'
    hotellink=set()
    
    for p in pageNum:
        print("page ",p)
        html=None
        
        
        if p==1: pageLink=url+cuisine
        else: pageLink=url+"&start="+str(p)+cuisine
        
        hotelnames = "HotelNames"+str(p)+".txt"
        fw=open(hotelnames,'w')
        flink=open('HotelLinks.txt','a')
        for i in range(5):
            try:
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html = response.content
                break;
            except Exception as e:
                print("failed ",i)
                time.sleep(5)
        
        if not html: continue;
        
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml')
        fw.write(str(soup))
        links = soup.findAll('span',{'class':'indexed-biz-name'})
        
        for link in links:
            hotellink=link.find('a')['href']
            
            flink.write(str(hotellink)+'\n');
        
    fw.close()


if __name__=='__main__':
    url='https://www.yelp.com/search?find_loc=Miami,+FL'
    run(url)
