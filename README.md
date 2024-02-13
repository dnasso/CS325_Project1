This program takes an input file containing 5 website urls that lead to news articles. It visits each of the articles, 
and strips the raw text of each article and saves them each into their own text files. These files are named numerically. 
The rest of this readme includes instructions for running this program yourself on your own device. If this readme is 
unsatisfactory, feel free to consult the main.py file, as it is meticulously commented.

Throughout this readme I will make referrences to the "target working directory." This program is meant to be entirely 
stored within its own folder. It doesn't currently have the ability to access a file in another directory, so please 
work entirely within the same directory for this project


1. Initialize the environment
    -This shouldn't be too easy. Download the requirements.yaml file into your target working directory.
    -It is important that you have Anaconda installed, otherwise, you cannot create the environment necessary to execute the code.
    -Simply type "conda env create -f requirement.yaml" into your terminal. It should work as desired.
2. Create your url file
    -The urls that you want to scrub need to be located in their own file.
    -Each url gets its own line. Don't include any extra whitespace. The first url should be on the first line.
    -The program is built to use websiteHTML.text as input. You can name your file differently so long as you
         change all mentions of that filename in main.py to whatever your new file is.
    -The websiteHTML.text file should be located in the same folder as main.py 
    -Don't include more than five urls. I, as I write this, have realized that I have built my code in such a way that
         it may only handle 5 urls at a time. It should still run, but it will likely only process the first 5 urls in
         the list.
   -Please make sure that the urls are all from the same website.
3. Inspect the website for its class_ attribute
    -This part may seem a little tricky at first, but its rather simply. Currently, the program works for articles written
         by the Guardian. The program works by scanning the html for <p> tags containing a specific class_ attribute. It
         then takes only the text from each inside each tag, and stores that in an output file.
    -The class_ variable currently in use is "dcr-1yh5nre". You may need to change this if you would like to use a different website.
    -To figure out what class_ variable you need, go to the website in question, and find the first actual paragraph of text in the
         article. From there, if you "right click->inspect" the paragraph, the element viewer should appear, and you should be able
         to easily see the <p> tag that the text is contained by. If the class_ variable is "dcr-1yh5nre", then great. You can proceed
         as normal. However, if the variable is different, you'll have to change all mentions of "dcr-1yh5nre" in main.py to whatever
         the new variable name is. 
4. Run main in the same directory as the url file
     -This should be pretty simple, but just type "python main.py" into the terminal. It may be different for you if you aren't on windows.
     -The program should run as intended.

Reminder: if the readme is less than satisfactory, feel free to consult main.py itself. The file is, hopefully, well-commented.
