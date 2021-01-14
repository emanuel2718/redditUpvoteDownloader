"""
Author: Emanuel Ramirez Alsina
Program: redditUpvoteDownloader
Description: Downloads user upvoted images from specific subreddits
"""

import argparse
import configparser
import os
from pathlib import Path
import pprint
import praw
import re
import requests

HOME_PATH = f'{Path.home()}/Pictures' # this will make the path ~/Pictures/

# Image downloading linmit
LIMIT = 500

class redditUpvoteDownloader:
    def __init__(self, sub):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.sub = sub

        self.path = f'{HOME_PATH}/{self.sub}/'
        #self.path = f'Pictures/{self.sub}/' # will make a foler Pictures/ inside this git repository
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                            client_secret=config['REDDIT']['client_secret'],
                            user_agent="Reddit Upvote Downloader",
                            username=config['REDDIT']['username'],
                            password=config['REDDIT']['password'])
        self.user = self.reddit.user.me()
        self.upvoted = self.user.upvoted(limit=LIMIT)

    def file_exists(self, filename):
        """Checks if file already exists or no"""
        if os.path.isfile(filename):
            print(f'Already Exists: {filename}')
            return True
        return False

    def download(self, filename, url):
        #TODO: only download .jpg or .png
        if self.file_exists(filename):
            return

        # TODO: refactor this
        # only add .png and .jpg files
        if not filename.endswith('.jpg') or not filename.endswith('png'):
            return

        r = requests.get(url)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f'New file added: {filename}')

    def run(self):
        #TODO: add error handling
        #images = []
        for item in self.upvoted:
            if item.subreddit == self.sub:
                filename = self.path + re.search('(?s:.*)\w/(.*)', item.url).group(1)
                self.download(filename, item.url)
                #print(f'Filename: {filename}')

def main():
    parser = argparse.ArgumentParser(description="Reddit Upvote Downloader by Emanuel Ramirez")
    req_args = parser.add_argument_group('Required Arguments')
    req_args = parser.add_argument('-s', type=str, help="subreddit", required=True)
    args = parser.parse_args()
    downloader = redditUpvoteDownloader(args.s)
    downloader.run()





if __name__ == '__main__':
    main()
