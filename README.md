<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Outliner Discord Bot

## About The Project
Outliner is a discord bot that answers questions from BCIT course outlines using OpenAI answer API. BCIT students are known to have immense workloads and may not always have time to manually check course outlines.  To solve this problem, our team built Outliner to help students be better informed while saving time.

<p align="right">(<a href="#top">back to top</a>)</p>

## Video Demo
https://youtu.be/D7p9ACDbYbA

<p align="right">(<a href="#top">back to top</a>)</p>

## Logic and Usage:
The bot must be provided with a list of links for 
the course outlines, and then initialized before being used. Initializing 
the bot will run the scraper module which scrapes the web pages of the 
course outlines for useful data. The data is then converted in to a 
text file which then goes to the ai_answers module, where the OpenAI 
works on the collected data and provides suitable answers to the questions.
Finally, the discord bot uses a user interface to ask and answer the questions.

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started:
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

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact:
Christie Tsang - [LinkedIn](https://www.linkedin.com/in/christietsang/)

Belal Kourkmas - [LinkedIn](https://www.linkedin.com/in/belal-kourkmas/)

Sepehr Zohoori Rad - [LinkedIn](https://www.linkedin.com/in/sepehr-zohoori-rad/)

Aditya Singh Attri  - [LinkedIn](https://www.linkedin.com/in/aditya3650/)

Project Link: [https://github.com/christietsang/nwHacks2022.git](https://github.com/christietsang/nwHacks2022.git)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/christietsang/nwHacks2022.svg?style=for-the-badge
[contributors-url]: https://github.com/christietsang/nwHacks2022/graphs/contributors
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/christietsang/
