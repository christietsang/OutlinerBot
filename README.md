# Outliner Discord Bot
January 16, 2022

## Developers: 
Aditya Singh Attri, Belal Kourkmas, Christie Tsang and Sepehr Zohoori Rad

## Description:
A discord bot that answers questions from BCIT course outlines using
OpenAI answer API. The bot must be provided with a list of links for 
the course outlines, and then initialized before being used. Initializing 
the bot will run the scraper module which scrapes the web pages of the 
course outlines for useful data. The data is then converted in to a 
text file which then goes to the ai_answers module, where the OpenAI 
works on the collected data and provides suitable answers to the questions.
Finally, the discord bot is used a user interface to ask and answer the questions.


### Commands:  
#### $upload  
Upload the lines after the command and store them in links.txt to be used for scraping.
For example:
```
>>> $upload
    https://www.bcit.ca/outlines/20221086158/
    https://www.bcit.ca/outlines/20221086157/
    https://www.bcit.ca/outlines/20221086155/
  
Links uploaded successfully!
```
#### $init
Initialize the bot by scraping the URLs provided in links.txt. For example:
```
>>> $init

Content generated successfully!
```
#### $ask
Ask the OpenAI API a question. For example:
```
>>> $ask How much is the midterm for procedural programmming worth?

25%
```