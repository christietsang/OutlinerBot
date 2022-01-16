import requests
from bs4 import BeautifulSoup
from header import generate_header


def open_file(file_name):
    with open(file_name) as file_object:
        string_list = []
        lines = file_object.read().splitlines()
        for url in lines:
            header = generate_header(url)
            data = get_data(url)
            soup = BeautifulSoup(data, "html.parser")
            stripped_data = parse_data(soup)
            tokenized_string = stripped_data.split()
            if len(tokenized_string) > 2000:
                sepehr_sucks = split_string(tokenized_string, header)
                string_list.extend(sepehr_sucks)
            else:
                string_list.append(stripped_data)

        name_file = "documents.txt"
        add_to_txt(string_list, name_file)


def split_string(data, header):
    initial_list = data.copy()
    final_list = []
    first_item = True
    while len(initial_list) > 1800:
        if first_item:
            final_list.append(" ".join(initial_list[0:1800]))
            first_item = False
        else:
            final_list.append(header + " ".join(initial_list[0:1800]))
        initial_list = initial_list[1800:-1]
    final_list.append(header + " ".join(initial_list[0:-1]))
    return final_list


def get_data(link):
    r = requests.get(link)
    return r.text


def parse_data(data):
    for information in data(["style", "script"]):
        information.decompose()

    return ' '.join(data.stripped_strings)


def add_to_txt(data, file_name):

    with open(file_name, 'w', encoding="UTF-8", errors="ignore") as file_object:
        file_object.write(f"{data}")


def main():
    open_file("information.txt")


if __name__ == '__main__':
    main()
