import re
from pdfminer.high_level import extract_pages, extract_text
import PyPDF2
import os

#Store pdf data into text variable
text = extract_text("NeverEatAlone.pdf")
organizedText = text 
#get current path of user
currentPath = os.getcwd()

#cleaning text
organizedText = organizedText.lower()
organizedText = re.sub(" ", "", organizedText)
organizedText = re.sub('\n', '', organizedText)
organizedText = re.sub(r'[^\w\s]', '', organizedText)
testText= extract_pages(organizedText[15])
print(testText)


folderName="KeithFerrazzi_Data"
#Create folder for user if needed
if not os.path.exists(folderName):
    os.makedirs(folderName)
else:
    print("KeithFerrazzi_Data folder already exists.")

#checking if a folder has been made in order 
if os.path.exists(folderName):
    #Everytime you add a new file make sure you change the filename so you don't overwrite old data.
    filename='NeverEatAlone.txt'
    #gets the current path to include the recently made folder
    path= os.path.join(currentPath ,folderName)
    #This is the path where the file will be written into
    fileWritePath = os.path.join(path, filename)
    #creating file
    with open(fileWritePath, 'w') as file:
        file.write(organizedText)