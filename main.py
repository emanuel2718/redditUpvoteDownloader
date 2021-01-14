""" Created by Emanuel Rmairez Alsina"""

import argparse
import configparser
import os
import pprint
import praw
import re
import requests

class redditUpvoteDownloader:
    def __init__(self, sub):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.sub = sub
        self.path = f'images/{self.sub}/'
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                            client_secret=config['REDDIT']['client_secret'],
                            user_agent="Reddit Upvote Downloader",
                            username=config['REDDIT']['username'],
                            password=config['REDDIT']['password'])
        self.user = self.reddit.user.me()
        self.upvoted = self.user.upvoted(limit=500)

    def file_exists(self, filename):
        if os.path.isfile(filename):
            print(filename)
            return True
        return False

    def download(self, filename, url):
        if self.file_exists(filename):
            return

        r = requests.get(url)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        with open(filename, 'wb') as f:
            f.write(r.content)

        print(f'New file added: {filename}')

    def run(self):
        images = []
        for item in self.upvoted:
            if item.subreddit == self.sub:
                filename = self.path + re.search('(?s:.*)\w/(.*)', item.url).group(1)
                self.download(filename, item.url)
                print(f'Filename: {filename}')

def main():
    parser = argparse.ArgumentParser(description="Reddit Upvote Downloader by Emanuel Ramirez")
    req_args = parser.add_argument_group('Required Arguments')
    req_args = parser.add_argument('-s', type=str, help="subreddit", required=False)
    args = parser.parse_args()
    downloader = redditUpvoteDownloader(args.s)
    downloader.run()





if __name__ == '__main__':
    main()
