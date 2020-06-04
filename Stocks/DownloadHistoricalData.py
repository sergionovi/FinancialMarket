# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:24:20 2020

Status: Able to get Bovespa Components

Objectives:
    
    Download and create a csv file with historical data 
    from all components (stocks) from bovespa.
    Required Libraries:
        Pandas
        yfinance 
        yahoofinancials
        
@author: Sergio Novi, sergiolnovi@gmail.com
"""
import requests
from lxml import html


# Step 1: Web-Scrap the list of all Bovespa components.
# We will need this list to download the data with yfinance

# Get page content from specific url
url = 'https://topforeignstocks.com/indices/components-of-the-bovespa-index/';
pageContent = requests.get(url);

# Store the contents under tree
tree = html.fromstring(pageContent.content)

# Take the data from the website table 
# ATTENTION: (this may not work if the website layout changes) 
table = tree.xpath('//*[@id="tablepress-2953"]/tbody')

bovespaComponents=[];
for i in range(len(table[0])):
    adress = '//*[@id="tablepress-2953"]/tbody/tr['
    adress = adress + str(i+1) + ']/td[3]/text()';
    
    bovespaComponents.append(tree.xpath(adress)[0]);

print(bovespaComponents)    


