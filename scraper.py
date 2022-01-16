"""
Scrape the BCIT course outline web page for useful content, and format it as a list of strings that can be used by the OpenAI ask API.
"""
import requests
from bs4 import BeautifulSoup


def generate_header(url: str) -> list[str, ...]:
    """
  Generate a header string containing important course identifiers.

  :param url: a string
  :precondition: string is a valid url
  :precondition: url can be parsed
  :postcondition: header is generated containing important information
  :return: a list containing important indentifying information
  """
    page = requests.get(url)
    # create beautiful soup object
    soup = BeautifulSoup(page.text, "html.parser")
    # identify HTML divs where data will be scraped
    header_list = [
        "outline__course-name",
        "outline__course-code",
        "outline__block outline__instructor-details"
    ]
    header = ""
    # strip script tags from text in header
    for index, element in enumerate(header_list):
        header_info = soup.find('div', attrs={"class": element})
        header += str(header_info.get_text())

    new_header = []
    # strip whitespace from text in header
    for whitespace in header:
        new_header.append(whitespace.replace("\n", " "))

    new_header = ''.join(new_header)
    return new_header


def generate_data(url: str, class_name: str) -> str:
    """
  Generate a list of strings from a class in a webpage that can be parsed by OpenAI.

  :param url: a string
  :param class_name: a string
  :precondition: url is a valid url
  :precondition: class_name contains a name of a class that exists in content of the provided url
  :postcondition: creates a string that contains the header followed by the information filtered from the class
  :return: a string containing the header followed by the information filtered from the class
  """
    page = requests.get(url)
    header = generate_header(url)
    soup = BeautifulSoup(page.text, "html.parser")
    new_data = []

    old_data = soup.find('div', attrs={"class": class_name})
    parsed_data = str(old_data.get_text())

    # clear whitespace in parsed data
    for whitespace in parsed_data:
        new_data.append(whitespace.replace("\n", " "))
    new_data = str(''.join(new_data))

    # join header with new data
    return header + new_data


def open_file(file_name: str) -> None:
    """
  Open a file containing class names and facilitate data generation.

  :param file_name: a string
  :precondition: documents.txt must exist and contain urls that contain the class names defined in class_names
  :postcondition: facilitates creation of documents.txt containing all the filtered data for OpenAI
  :return: None 
  """
    with open(file_name) as file_object:
        # split URL links by line
        lines = file_object.read().splitlines()
        # identify divs where data will be scraped
        class_names = [
            "outline__block outline__details",
            "outline__block outline__outline-sections",
            "outline__block outline__course-description",
            "outline__block outline__learning-outcomes"
        ]
        full_data_list = []
        # append web-scraped data to an empty list
        for url in lines:
            for class_name in class_names:
                full_data_list.append(generate_data(url, class_name))
        name_file = "documents.txt"
        # call function to write data to text file
        add_to_txt(full_data_list, name_file)


def add_to_txt(data: list[str, ...], file_name: str) -> None:
    """
  Write a text file that contains filtered, web-scraped data.

  :param data: a list of strings containing the web-scraped data
  :param file_name: the name of the file for the data to be written to
  :precondition: data must be a list of strings
  :precondition: file_name must be a string with a file extension
  :postcondition: creates a file that contains filtered, web-scraped data as a list with string elements
  :return: None
  """
    # create text file and write web scraped data
    with open(file_name, 'w', encoding="UTF-8",
              errors="ignore") as file_object:
        file_object.write(f"{data}")


def generate_content() -> None:
    """
  Begin scraping for OpenAI.await
  :precondition: links.txt exists in the same directory and contains a valid url on each line
  :postcondition: begin scraping for OpenAI using links.txt
  :return: None
  """
    open_file("links.txt")
