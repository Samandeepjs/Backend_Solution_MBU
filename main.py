import urllib.request as requests
import json
import os
import sys


def get_posts(user_start, user_end, file):
    # To use request package in current program
    response = requests.urlopen("http://jsonplaceholder.typicode.com/posts")
    d = response.read()
    data = json.loads(d)
    fh = open(file, 'w')
    for i in data:
        if i['userId'] in range(int(user_start), int(user_end)):
            fh.write(f"{i}")
            print("Post:")
            print(f"{i}")  # Press Ctrl+F8 to toggle the breakpoint.




if __name__ == '__main__':
    arguments = len(sys.argv) - 1
    loc = 1
    val = [0, 1, 11, "stdout.txt"]
    while arguments >= loc:
        val[loc] = sys.argv[loc]
        # print(val[loc])
        loc = loc + 1
    get_posts(val[1], val[2], val[3])
