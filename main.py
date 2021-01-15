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
#LIMIT = 500 # limit for the amount of upvoted posts to check

class redditUpvoteDownloader:
    def __init__(self, sub, limit, debug):
        """ Intializer

        :param: string: the subreddit name given as an argument with the -s flag
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.amount_of_upvotes_scanned = 0
        self.debug = debug
        self.sub = sub
        self.limit = limit # can't cast here because limit could be None
        self.download_counter = 0
        self.path = f'{HOME_PATH}/{self.sub}/'
        #self.path = f'Pictures/{self.sub}/' # will make a foler Pictures/ inside this git repository
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                            client_secret=config['REDDIT']['client_secret'],
                            user_agent="Reddit Upvote Downloader",
                            username=config['REDDIT']['username'],
                            password=config['REDDIT']['password'])
        self.user = self.reddit.user.me()
        self.upvoted = self.user.upvoted(limit=None)

    def file_exists(self, filename):
        """Checks if file already exists or no

        :param: string: file name
        :return: bool: file already exists in the current path folder or not
        """
        if os.path.isfile(filename):
            print(f'Already Exists: {filename}')
            return True
        return False

    def is_file_an_image(self, filename):
        """ Check if file is a valid image with a valid extension
            Extensions currently supported: .png, .jpg, .jpeg

        :param: string: file name
        :return: bool: is file an image or not
        """
        if filename.endswith(('.jpg', '.png', 'jpeg')):
            return True
        return False

    def download(self, filename, url):
        """ Downloads the image if the image is not already downloaded and if it is
            a valid image with a valid extension (some posts don't link to an image,
            instead they link to a website that holds the image)
        """
        if self.file_exists(filename):
            return

        if not self.is_file_an_image(filename):
            return

        r = requests.get(url)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f'New file added: {filename}')

    def check_download_limit(self):
        """ Check the image download limit given by the user with the -l flag.
            If there was no -l flag given this will always return True.
            If the -l flag was found; check if the download limit has been reached or not.
        """
        if self.limit is None or self.download_counter < self.limit:
            return True
        return False

    def run(self):
        """ Iterate through all the user upvoted posts (withting the @LIMIT) and call for download
            if the subreddit matches the given subreddit by the user through the -s argument.
        """
        for item in self.upvoted:
            self.amount_of_upvotes_scanned += 1
            if item.subreddit == self.sub:
                if self.check_download_limit():
                    filename = self.path + re.search('(?s:.*)\w/(.*)', item.url).group(1)
                    self.download(filename, item.url)
                    self.download_counter += 1
                else:
                    break
        print(f'\nDone: {self.download_counter} images downloaded into {self.path}')

        if self.debug:
            print(f'Amount of upvoted posts scanned: {self.amount_of_upvotes_scanned}')
        return

def main():
    parser = argparse.ArgumentParser(description="Reddit Upvote Downloader by Emanuel Ramirez")
    parser.add_argument_group('Required Arguments')
    parser.add_argument('-debug', '--debug', action='store_true', help="Debug flag", required=False)
    parser.add_argument('-s', type=str, help="subreddit", required=True)
    parser.add_argument('-t', type=str, help="Upvoted or Savedposts?", required=False)
    parser.add_argument('-l', type=int, help="Limit of post to download (default: None)", required=False)
    args = parser.parse_args()
    downloader = redditUpvoteDownloader(args.s, args.l, args.debug)
    downloader.run()


if __name__ == '__main__':
    main()
