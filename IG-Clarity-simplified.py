
import argparse
import zipfile
from bs4 import BeautifulSoup

def extractor(filename):
    with open(filename, "r") as file:
        readfile = file.read()

    soup = BeautifulSoup(readfile, 'html.parser')
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
        source.extractall("temp_files/")
        following = extractor("temp_files/connections/followers_and_following/following.html")
        follower = extractor("temp_files/connections/followers_and_following/followers_1.html")

        listed = []
        for i in following:
            if i not in follower:
                listed.append(i)
        
        

    return listed

def program():
    path_for_file = input("Enter the complete path of file: ")

    print("These ppl didn't follow you back!")
    for i in logic(path_for_file):
        print(i)

program()