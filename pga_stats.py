import requests
from bs4 import BeautifulSoup
import pandas as pd
from functools import reduce, partial

#Stat page suffixis from PGATOUR.com to pick which data we want to scrape

base_url = "https://www.pgatour.com/stats/"

stats_id = []
# creating an empty list 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = str(input()) 
    stats_id.append(ele) # adding the element 

print("Scapppy TIME")
d = {}
#scapes each stats page based on which pages are specified
for pages in stats_id:
    print(base_url+"stat."+str(pages)+".html")
    d[pages] = pd.read_html(base_url+"stat."+str(pages)+".html", header=0)[1]
    
my_reduce = partial(pd.merge, on='PLAYER NAME', how='outer')
data = reduce(my_reduce, d.values())

data.to_csv('stats_list_1.csv', index = False)
print(data,"\n Success")