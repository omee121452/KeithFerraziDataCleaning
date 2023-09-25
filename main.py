import re
from pdfminer.high_level import extract_pages, extract_text
import PyPDF2
import os

text = extract_text("NeverEatAlone.pdf")
organizedText = text 
currentPath = os.getcwd()

#make all text lower case
organizedText = organizedText.lower()
#remove white space
organizedText = re.sub(" ", "", organizedText)
organizedText = re.sub('\n', '', organizedText)
#remove Punctuation
organizedText = re.sub(r'[^\w\s]', '', organizedText)
testText= extract_pages(organizedText[15])
print(testText)


folderName="KeithFerrazzi_Data"

if not os.path.exists(folderName):
    os.makedirs(folderName)
else:
    print("KeithFerrazzi_Data folder already exists.")

#Everytime you add a new file make sure you change the filename to something different so then you don't overwrite old data.
if os.path.exists(folderName):
    filename='NeverEatAlone.txt'
    path= os.path.join(currentPath ,folderName)
    print(path)
    fileWritePath = os.path.join(path, filename)
    with open(fileWritePath, 'w') as file:
        file.write(organizedText)