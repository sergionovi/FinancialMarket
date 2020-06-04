# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:24:20 2020

Status: NOTHING IS WORKING

Objectives:
    
    Download and create a csv file with historical data 
    from all components (stocks) from bovespa.
    Required Libraries:
        Pandas
        yfinance 
        yahoofinancials
        
@author: Sergio Novi, sergiolnovi@gmail.com
"""
# Basic Libraries to download and read the data
import requests
from lxml import html

pageContent = requests.get('https://topforeignstocks.com/indices/components-of-the-bovespa-index/')
#Store the contents of the website under doc
tree = html.fromstring(pageContent.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = tree.xpath('//*[@id="tablepress-2953"]/tbody')


# Website for learning about how to scrab 
# data from websites
# https://3583bytesready.net/2016/08/17/scraping-data-python-xpath/



