### 
# So here in this file, we import the fileManager module which 
# contains the body of the project. The only item from module 2 
# is the parser declaration. The variables initialized here are 
# items that I wanted to be able to keep flexible. These include 
# file paths, the parser keyword, and even the class used to 
# initialize the parser. There are a couple test functions defined, 
# but these exist simply to test that the filepaths can be found. 
# Past all the initialization, you see three function calls from 
# the file manager. All of the work of this program is encapsulated 
# by those three functions.
###

#Imports
from module_1 import fileManager

#File Paths
dataIn = "./Data/raw/websiteHTMLs.txt"  #input path
dataOut = "./Data/processed/"   #output path

#This is the key we use identify the body paragraphs of the website. 
# I'm not sure where to put this, but by keeping it out here, its 
# not hardcoded into the class objects.
parserKey = "dcr-1yh5nre"

#This is a test of the input path
def testIn():
    fileRead = open("./Data/raw/websiteHTMLs.txt", "r")
    fileRead.close()

#This is a test of the output path
def testOut():
    fileWrite = open("./Data/processed/test.txt", "w")
    fileWrite.write("This is a test")
    fileWrite.close()

#Custom Class Objects
parser = fileManager.articleParser.articleParser(parserKey) #This may be the most disgusting function call I've ever seen. I'm sorry
manager = fileManager.fileManager(parser, dataIn, dataOut)

#Function Calls
manager.readHtml()
manager.getArticles()
manager.saveArticles()