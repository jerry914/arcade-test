import os
import mcConvert

projectName = "block-out"
url = 'https://raw.githubusercontent.com/microsoft/pxt-arcade/master/docs/lessons/'+projectName+'.md'

try:
    os.mkdir("output/makecode/"+projectName)
except Exception as e:
    print(e)

mcConvert.md_convert(projectName,url)