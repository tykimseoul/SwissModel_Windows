from bs4 import BeautifulSoup
import os

names = []
fileNames=[]
for i in os.listdir('./done'):
    if i.endswith('.html'):
        print(i)
        fileNames.append(i)

for filename in fileNames:
    with open('./done/' + filename, "r") as file:
        soup = BeautifulSoup(file, 'html.parser')
        titles = soup.select("div.container-fluid > div.col-sm-8 > span")
        for title in titles:
            t = title.find("a").getText()
            names.append(t)
print(len(names))

def getDoneNames():
    return names