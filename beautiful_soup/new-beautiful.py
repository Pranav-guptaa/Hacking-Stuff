# Reference link ::::: https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
files = open("beautiful.txt","w")
files.write(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(results.prettify())
files_out = open("id.txt","w") 
files_out.write(str(results))
# https://realpython.com/beautiful-soup-web-scraper-python/
job_elements = results.find_all("div", class_="card-content")
#print(job_elements)
'''
for job_element in job_elements:
    print(job_element, end="\n"*2)'''
'''
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()
'''
'''

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

'''
python_jobs = results.find_all("h2", string="Python")
print(python_jobs)
