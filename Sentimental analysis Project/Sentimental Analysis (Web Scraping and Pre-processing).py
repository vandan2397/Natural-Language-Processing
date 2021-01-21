# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:27:31 2021

@author: Vandan
"""


# install lxml (parser)
# install html5lib (parser)

# install beautiful soup for webscraping
from bs4 import BeautifulSoup

# install requests to connect to urls
import requests

# install pandas for analysis
import pandas as pd



class WebScraping():
    
    
    # Function to get links of all pages
    def get_links():
        
        # Links of all pages
        links = []
        
        for i in range(1,238):
            links.append("https://www.consumeraffairs.com/online/amazon.html?page="+str(i))
        
        return links


    # Function to get data from all pages
    def Scraping(links):
        

        # list for rating
        rating_list = []


        # list for review
        review_list = []

        for i in links:
            source = requests.get(i).text
            soup = BeautifulSoup(source,'lxml')
        
            # Extracting reviews by customers
            for article in soup.find_all('div',class_='rvw js-rvw'):
                review = article.find('div', class_='rvw-bd')
                review_list.append(review.text)
            
            # Extracting ratings by customers
            for article1 in soup.find_all('div',class_='rvw__hdr-stat'):
                #ratings
                rating_list.append(article1.find('meta',itemprop='ratingValue')['content'])

        
        # Creaing dataframes of both list
        rating_df = pd.DataFrame(rating_list)
        review_df = pd.DataFrame(review_list)
        
        # Combining Dataframe
        data = pd.concat([rating_df,review_df],axis=1)
        return data
    
    
    # Function for preprocessing of data
    def Preprocess(data):
        
        # drop insignificant column
        data.drop('Unnamed: 0',axis=1,inplace=True)

        # Rename columns
        data.columns = ['Reviews','Ratings']
        
        
        #manipulating values using lambda function
        data['Reviews_1'] = data['Reviews'].apply(lambda x: x.replace('Original review:',''))
        
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2011','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2012','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2013','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2014','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2015','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2016','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2017','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2018','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2019','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2020','',1))
        data['Reviews_1'] = data['Reviews_1'].apply(lambda x: x.replace('2021','',1))
        
        
        # Extracting data which has ratings along with review
        data = data.iloc[0:6621,:]
        
        # Dropping old Reviews column
        data.drop('Reviews',axis=1,inplace=True)
        
    
        # labelling ratings

        # Ratings to label
        def tenure_lab(data) :
            if data["Ratings"] <= 3 :
                return "Bad"
            elif (data["Ratings"] >= 4) :
                return "Good"
         
        data["Ratings"] = data.apply(lambda data:tenure_lab(data), axis = 1)
        
        data.columns = ['Ratings','Reviews']
        
        return data

webscrap = WebScraping()

# calling getlinks method
links = webscrap.get_links()

# calling Scraping function
data = webscrap.Scraping(links)

# calling preprocess method
file = webscrap.Preprocess(data)

file.to_csv('Amazon_reviews.csv') 
    