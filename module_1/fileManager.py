### 
# This is the fileManager. This object handels inbound and outbound data. 
# It has a parser object attached so it can do work on the data and save the 
# output. The parser object is declared in module 2, and most of the work 
# is done there. This file is focused entirely on taking in raw data, and 
# spitting out processed data. The htmls are all read together an saved to 
# list. This list is then iterrated over with by the parser. For each html, 
# the parser returns the entirety of an article as a string object which is 
# appended to fileManager's internal article string list. This list is then 
# iterated over, with each article being numbered and saved to its own text 
# file. Currently, each output file has firstline: Name and secondline: 
# article, with and \n removed from the article. It's not entirely conveniant 
# to read.
### 
# This is a display of the "Open-Closed Principle". The parser class has 
# two generic methods used by the fileManager. As long as these methods are 
# implemented, new variants of the parser class could be written and 
# substituted without changing any of the code here.
###



from module_2 import articleParser

class fileManager():
        def __init__(self, parser, fileInPath, fileOutPath):
            #self.parser = articleParser use Observer method to use parser to alter these items
            self.parser = parser
            self.htmlList = []
            self.articleList = []
            self.fileInPath = fileInPath
            self.fileOutPath = fileOutPath
        def readHtml(self):
            fileRead = open(self.fileInPath, 'r')
            hrefList = fileRead.readlines()
            for href in hrefList:
                #print("Another test")
                #print(href)
                href = href.strip()
                #print(href)
                self.htmlList.append(href)
        def saveArticles(self):
            articleID = 0
            for article in self.articleList:
                articleID += 1
                fileWriteName = self.fileOutPath + "Article_" + str(articleID) + ".txt"
                articleTitle = "Article " + str(articleID)

                fileWrite = open(fileWriteName, "w", encoding="utf-8")
                fileWrite.write(articleTitle + ":\n")
                fileWrite.write(article)
                fileWrite.close()

                if (articleID >= 20):
                    break
        def getArticles(self):
            for html in self.htmlList:
                #print("Why do my creations fail me")
                #print(html)
                self.articleList.append(self.parser.htmlScrub(html))

print("fileManager.py imported successfully")