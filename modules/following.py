from bs4 import BeautifulSoup


def followings(filename):
    with open(filename, "r") as file:
        readfile = file.read()

    soup = BeautifulSoup(readfile, 'html.parser')
    a_elements = soup.find_all('a')

    following_list = []
    for a in a_elements:
        following_list.append(a.text)

    return following_list
