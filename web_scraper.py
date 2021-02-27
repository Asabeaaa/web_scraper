import pandas as pd
import requests
from bs4 import BeautifulSoup


title=[]
company=[]
location=[]

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer') 
#print(results.prettify()) #view all html content on website

job_elems = results.find_all('section', class_='card-content')
# for job_elem in job_elems:
#     print(job_elem, end='\n'*2) #print all diff elements stored in card-content class

#Extracting text data from html
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    title.append(title_elem.text.strip())
    company.append(company_elem.text.strip())
    location.append(location_elem.text.strip())

df = pd.DataFrame({'Job description':title,'Company':company,'Location':location}) 
df.to_csv('jobs.csv')
print(df)










