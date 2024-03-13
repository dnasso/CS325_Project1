### 
# This module contains the definition for the parser and articleParser class. 
# The parser class is just a template. Because the articleParser is mostly 
# dependent on BeastifulSoup, I felt this was the most important part of 
# the project to implement the ability to write a new parser object in 
# the future. The parser needs a keyword which will be passed to it by 
# the module that calls it. I found this keyword by manually inspecting 
# the elements I wanted to scrub from the site I wanted to scrub. Whichever 
# module calls the parser must pass the parser an html for it to pull contents 
# from. In the current implementation, the keyword is declared outside the 
# scope and may be changed, but articleParser cannot is dependent on BeatifulSoup, 
# and as such this cannot be changed without implementing a new parser object. 
# With the current keyword declared in main, the parser will return the article 
# contents from whichever html it is fed.
### 
# This is a display of the "Open-Closed Principle". The parser class has two 
# generic methods used by the fileManager. As long as these methods are implemented, 
# new variants of the parser class could be written and substituted without changing 
# any of the code here.
###


from bs4 import BeautifulSoup
import requests
#import html5lib

class parser():
    def __init__(self, parserKey):
        raise NotImplementedError
        #print("Undefined Parser")
        #pass
    def htmlScrub(self, html):
        raise NotImplementedError
        #print("Undefined Parser")
        #pass

class articleParser(parser):
        def __init__(self, parserKey):
            #self.fileManager = fileManager
            self.parserKey = parserKey
        
        def htmlScrub(self, html):
            #print("We've made it this far without error :P")
            #print(html)

            r1 = requests.get(html)
            print(r1.status_code)
            webPage = r1.content

            soup = BeautifulSoup(webPage, 'html5lib')
            #webPageContent = soup.find_all('p', class_='dcr-1yh5nre')
            webPageContent = soup.find_all('p', class_=self.parserKey)
            article = ""
            for paragraph in webPageContent:
                article += paragraph.get_text()
            #print(article)
            return article

print("articleParser.py imported successfully")