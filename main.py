# Install All Requirements
#1. pip install requests
#2. pip install bs4
#3. pip install htmllib5




import requests
from bs4 import BeautifulSoup


url="https://www.beingguru.com/"

# Step 1: Get The HTML

r=requests.get(url)
# print(r.text)
htmlContent= r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup= BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# Step3: HTML Tree Traversal
# Commonly Used type of Objet 
# print(title)  #1. Tag
# print(title.string)  # 2. NavigableString
# print(soup)   # 3. Beautysoup
# 4. Comments



# Get the Title of HTML Page
title= soup.title
# print(title)

# Get the All Paragraphs of HTML page
pra= soup.find_all('p')




# Get the first element of HTML page
prag= soup.find('p')

# Get classes of any element of HTML page
pClass= soup.find('p')['class']
# print(pClass)

# Find all the elements with class'lead' of HTML page
elementWithclassLead= soup.find_all("p",class_= "lead")
# print(elementWithclassLead)


# Get text from tags/soup
print(soup.find('p').get_text())


# Get the All Anchor tag of HTML page
ach= soup.find_all('a')
allLinks= set()
#Get the links
for link in ach:
    if(link.get('href')!= '#'):
        linkText= "https://www.beingguru.com" + link.get('href')
        allLinks.add(link)
        print(linkText)






