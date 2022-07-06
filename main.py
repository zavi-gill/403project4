import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Student/Downloads/chromedriver.exe')
driver.get('https://oxylabs.io/blog')

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)


for a in soup.findAll(attrs='css-1dmex2s e1kk1ckf2'):
    name = a.find('h5')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-1dmex2s e1kk1ckf2'):
    description = b.find('p')
    if description not in results:
        other_results.append(description.text)


df = pd.DataFrame({'Names': results, 'Description': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
