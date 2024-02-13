### This is where most of the work will be done.

### urllib was considered early for the project, but ultimately 
### it was deemed unfit for the project. It did not fit the 
### project's needs. The package is still lurking within the 
### environment, but only as legacy piece that I have yet to purge.

#import urllib.request
import requests #needed installing
from bs4 import BeautifulSoup #needed installing
import html5lib

fileRead = open("websiteHTMLs.txt", "r")

# This for loop is mostly for labeling the article files numerically
for i in range(1,6):
    
    # This print statement lets me know which article the program is 
    # iterating over. It helps where issues occur
    print(f"Iteration {i}:")

    # This pulls a single url from the url file along with a little 
    # whitespace that we will need to trim up
    href = fileRead.readline()
    
    # This removes the whitespace
    href = href.strip()

    # This print statement is for bug-fixing. It lets me see that 
    # the url has been read successfully.
    print(href)

    # This returns a custom object that contains the website's content. 
    # I used the variable name r1 purely as a holdover from a tutorial
    # I followed.
    r1 = requests.get(href)

    # r1.status_code returns the status_code from the pull. Printing it
    # lets me see whether the connection was successful or not while debugging.
    print(r1.status_code)

    # r1.content is a string. This is a part of the code I do not fully understand.
    # Printing it returns the website's html in format b"****". I'm not familiar with
    # b strings but I understand that we need to do work on this object to render it usable.
    webPage = r1.content

    # BeautifulSoup removes the html from the b string. If soup is printed, it prints the string
    # with proper formatting. For example, if the b string was b"**\n**", printing soup would print:
    # "**
    # **"
    soup = BeautifulSoup(webPage, 'html5lib')

    # I don't know what library find_all is from, but it iterates over the 
    # soup string with two arguments. It takes a type of html tag, and a 
    # class variable. It finds all html tags that match the tag and class, 
    # and returns the content inbetween the tags. In this context, class 
    # 'dcr-1yh5nre' was the class associated with the articles actual 
    # content on the guardian. I don't know its significance, but it is 
    # incredibly useful.
    webPageContent = soup.find_all('p', class_='dcr-1yh5nre')
    
    # This is where we initialize the file name for the sake of organization
    fileWriteName = "Article_" + str(i) + ".txt"
    
    # A couple things here. First, we are creating the file if it doesn't 
    # exist. If it does, we are overwriting it with this message so that 
    # we don't accidentally append the same article to the same file every 
    # time we run the program.
    fileWrite = open(fileWriteName, "w", encoding="utf-8")
    
    # Just loads a title into the file to initialize it.
    fileWrite.write(fileWriteName + ":\n")

    # We close the file so that we may now append to it. I understand 
    # that this may be unnecessary, but with my lack of experience with 
    # read/write operations, I felt it was better to be cautious in my 
    #application here.
    fileWrite.close()
    
    #find_all() returned all the paragraphs in a list, so we simply 
    # iterate over that list, and append each item to the text file we 
    # are storing these in. All of the paragraphs are stored in line 2.
    for paragraph in webPageContent:
        fileAppend = open(fileWriteName, "a", encoding="utf-8")
        fileAppend.write(paragraph.get_text())
        fileAppend.close()