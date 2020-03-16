import json
from pprint import pprint
import generator

def JSON_openTemplete():
    with open("src\Templete\JSONtemplete.txt", 'r',encoding = 'utf8') as tf: 
        templete = tf.read()
        tf.close()
        return templete

def JSON_open(fileName):
    with open(fileName+".txt", 'r',encoding = 'utf8') as f: 
        data = f.read()
        f.close()
        return data

def JSON_write(content,fileName):
    with open(fileName+".txt", 'w',encoding = 'utf8') as f: 
        f.write(content)
        # print(templete)
        f.close()

def JSON_generate(fileName,sectionText,subtitle,sectionImgCount,sectionBubbleCount,route,sectionVideoCount,videoLink):
    templete = JSON_openTemplete()
    content = templete.replace('CONTENTTITLE',generator.titleSplit(sectionText[0],subtitle))
    content = content.replace("SUBTITLE",subtitle)
    content = content.replace("SECTION[1]",sectionText[1])
    content = content.replace("[[☃ article-block 1~SECTIONLEN-2]]",generator.artBlk_generate(len(sectionText)-2,'a'))
    content = content.replace("ARTICLEBLOCK",generator.cont_wiget_generate(sectionText,sectionImgCount,sectionBubbleCount,route,sectionVideoCount,videoLink))
    JSON_write(content,fileName)


# JSON_open('output/getstart/基礎電學觀念')
