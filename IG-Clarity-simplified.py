import os
import sys
import zipfile
from bs4 import BeautifulSoup


def extractor(content):
    soup = BeautifulSoup(content, 'html.parser')
    a_elements = soup.find_all('a')

    people_list = []
    for a in a_elements:
        people_list.append(a.text)

    del soup, a_elements

    return people_list


def logic(path) -> list:
    """

    :rtype: object
    """
    with zipfile.ZipFile(path, "r") as source:
        with source.open("connections/followers_and_following/following.html") as following_file:
            following = extractor(following_file.read())
        with source.open("connections/followers_and_following/followers_1.html") as follower_file:
            follower = extractor(follower_file.read())

        listed = []
        for i in following:
            if i not in follower:
                listed.append(i)

    return listed


def program():
    try:
        path_for_file = sys.argv[1]
    except:
        print("You did not define file\nReading zip file from current directory\n")
        try:
            files = [file for file in os.listdir(os.getcwd()) if file.lower().endswith(".zip")]
            path_for_file = files[0]
        except:
            print("Zip file does not exist in current directory?\n")

    try:
        print("These ppl didn't follow you back!")
        for i in logic(path_for_file):
            print(i)
    except:
        print("The process failed. Check the file location or ensure the zip file is in same directory as this script")


program()
