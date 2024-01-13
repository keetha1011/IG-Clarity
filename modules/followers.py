from bs4 import BeautifulSoup


def followers(filename):
    with open(filename, "r") as file:
        readfile = file.read()

    soup = BeautifulSoup(readfile, 'html.parser')
    a_elements = soup.find_all('a')

    follower_list = []
    for a in a_elements:
        follower_list.append(a.text)

    return follower_list
