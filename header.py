import requests
from bs4 import BeautifulSoup


def generate_header(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    header = str(soup.find('div', attrs={"class": "outline__course-name"}))
    header += str(soup.find('div', attrs={"class": "outline__course-code"}))
    header += str(soup.find('div', attrs={"class": "outline__course-code"}))

    return header
