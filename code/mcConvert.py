import marko
import requests
from bs4 import BeautifulSoup
import junyiJSONgenerate
import os
import re
import csv

def trLatex(color,key): 
    return r'$\\require{enclose}\\enclose{box}[mathcolor="'+color+r'",mathbackground="'+color+r'"]{\\color{white}{'+key+r'}}\\\\$'

def addColor(tag,key):
    if(tag == "sprites"):
        return trLatex("#4b7bec",key)
    elif(tag == "controller"):
        return trLatex("#d54322",key)
    elif(tag == "game"):
        return trLatex("#8854d0",key)
    elif(tag == "scene"):
        return trLatex("#4b6584",key)
    elif(tag == "info"):
        return trLatex("#cf6a87",key)
    elif(tag == "loops"):
        return trLatex("#20bf6b",key)
    elif(tag == "logic"):
        return trLatex("#45aaf2",key)
    elif(tag == "variables"):
        return trLatex("#ec3b59",key)
    elif(tag == "math"):
        return trLatex("#a55eea",key)
    elif(tag == "functions"):
        return trLatex("#1446a0",key)
    else:
        return trLatex("black",key)
        

def md_convert(projectName,url):

    resp = requests.get(url)

    content = resp.text
    # conText = cc.convert(conText)
    # conText = translator.translate(conText, src='en',dest='zh-tw').text

    if not os.path.isdir("output/makecode/"+projectName):
        os.mkdir("output/makecode/"+projectName)

    pages = content.split("## Part")
    
    step = 0
    scriptIdx = 0
    for p in pages:
        templete = junyiJSONgenerate.JSON_open('src\Templete\JSONempty')
        content = p.replace("\n","\\n")
        content = content.replace('"','\\"')
        content = "#"+content
        iframeIdx = 0
        iframeBlock = ''
        while 1:
            if(content.find("```")==-1):
                break
            pre = content.find("```",0)
            content = content.replace("```","",1)
            bac = content.find("```",0)
            content = content.replace("```","",1)
            # script = content[pre:bac]
            try:
                content = content[:pre]+"[[☃ iframe %s]]\\n\\n[[☃ iframe %s]]"%(iframeIdx*2+1,iframeIdx*2+2)+content[bac:]
                scriptIdx +=1
                iframeUrl = "https://jerry914.github.io/arcade-test/"+projectName+"/"+str(scriptIdx)+".html"
                ifTemplete = junyiJSONgenerate.JSON_open('src\Templete\JSONiframe')
                iframeBlock += ifTemplete.replace("https://ys-fang.github.io/Linkit7697Learning-Resources/bubble/ROUTE/BUBBLEIDX.html",iframeUrl)
                iframeBlock = iframeBlock.replace("IFRAMEIDX",str(iframeIdx*2+2))
                iframeIdx +=1
            except Exception as e:
                print(e)
        content = content.replace("`","")
        while 1:
            if(content.find("|")==-1):
                break
            pre = content.find("|",0)
            content = content.replace("|","",1)
            if(content[pre]=='|'):
                content = content.replace("|","",1)
            bac = content.find("|",0)
            content = content.replace("|","",1)
            if(content[bac]=='|'):
                content = content.replace("|","",1)
            tag = content[pre:bac].split(":")[0]
            try:
                keyword = content[pre:bac].split(":")[1]
                content = content[:pre]+addColor(tag,keyword)+content[bac:]
            except Exception as e:
                print(e)
        content = content.replace('"','\\"')
        output = templete.replace("CONTENT",content)
        if(output.find("iframe")==-1):
            output = output.replace("WIDGETS","")
        else:
            output = output.replace("WIDGETS",iframeBlock[:-1])
        junyiJSONgenerate.JSON_write(output,"output/makecode/"+projectName+"/"+str(step))
        step+=1
        output = output.replace("\n","")
        with open('output/junyi.csv','a+', newline='',encoding = 'utf8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['0','False','電腦科學','',projectName,'1',output,'',''])
        csvfile.close()