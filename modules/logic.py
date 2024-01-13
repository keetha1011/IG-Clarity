import zipfile
from modules.following import followings
from modules.followers import followers


def logic(path) -> list:
    """

    :rtype: object
    """
    with zipfile.ZipFile(path, "r") as source:
        source.extractall("temp_files/")
        following = followings("temp_files/connections/followers_and_following/following.html")
        follower = followers("temp_files/connections/followers_and_following/followers_1.html")

        listed = []
        for i in following:
            if i not in follower:
                listed.append(i)

    return listed
