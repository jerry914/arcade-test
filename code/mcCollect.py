import requests
from bs4 import BeautifulSoup
import junyiJSONgenerate
import re

projectName = 'cherry-pickr'
url = "https://arcade.makecode.com/lessons/"+projectName
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
content = soup.text
pointer = 0

codeBlock = soup.find_all("code", class_="lang-blocks")

sctIdx = 0
for b in codeBlock:
    sctIdx+=1
    sct = str(b.text)
    with open("D:/workspace/arcade-test/"+projectName+"/"+str(sctIdx)+".html", 'w',encoding = 'utf8') as f: 
        f.write(junyiJSONgenerate.JSON_open("Templete/script").replace("SCRIPT",sct))
        f.close()
