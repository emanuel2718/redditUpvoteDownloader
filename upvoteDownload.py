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
    def __init__(self, sub, limit, user=False, debug=False):
        """ Intializer

        :param: string: the subreddit name given as an argument with the -s flag
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.amount_of_upvotes_scanned = 0
        self.debug = debug
        self.by_user = user
        self.sub = sub
        self.path = None
        self.limit = limit
        self.download_counter = 0
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                            client_secret=config['REDDIT']['client_secret'],
                            user_agent="Reddit Upvote Downloader",
                            username=config['REDDIT']['username'],
                            password=config['REDDIT']['password'])
        self.user = self.reddit.user.me()
        self.upvoted = self.user.upvoted(limit=None)

        if self.sub is not None:
            self.path = f'{HOME_PATH}/{self.sub}/'
            #self.path = f'Pictures/{self.sub}/' # will make a foler Pictures/ inside this git repository
        else:
            self.path = f'{HOME_PATH}/{self.user}/'

    def file_exists(self, filename, item):
        #TODO: change this docstring. Signature changed.
        """Checks if file already exists or no

        :param: string: file name
        :return: bool: file already exists in the current path folder or not
        """
        # could be present with or without the username in front
        image_name = re.search('(?s:.*)\w/(.*)', item.url).group(1)
        filename_with_username = self.path + str(item.author) + '_' + image_name
        filename_without_username = self.path + image_name

        #TODO: Refactor me!
        if os.path.isfile(filename_without_username):
            if self.by_user:
                print(f'Adding {item.author} (username) to {image_name} file.')
                os.rename(filename_without_username, filename_with_username)
                return True
            else:
                return True
        elif os.path.isfile(filename_with_username):
            if not self.by_user:
                print(f'Removing username from {filename} file.')
                os.rename(filename_with_username, filename_without_username)
                return True
            else:
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

    def download(self, filename, item):
        #TODO: change this docstring. The parameters has changed. Now we pass the entire post item
        """ Downloads the image if the image is not already downloaded and if it is
            a valid image with a valid extension (some posts don't link to an image,
            instead they link to a website that holds the image)
        """
        # -s subreddit flag given but the current subreddit doest not match
        if self.sub is not None and item.subreddit != self.sub:
            return

        if self.file_exists(filename, item):
            return

        if not self.is_file_an_image(filename):
            return

        r = requests.get(item.url)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f'New file added: {filename}')
        self.download_counter += 1

    def check_download_limit(self):
        """ Check the image download limit given by the user with the -l flag.
            If there was no -l flag given this will always return True.
            If the -l flag was found; check if the download limit has been reached or not.
        """
        if self.limit is None or self.download_counter < self.limit:
            return True
        return False

    def get_filename(self, item):
        if self.by_user:
            return self.path + str(item.author) + '_' + re.search('(?s:.*)\w/(.*)', item.url).group(1)
        return self.path + re.search('(?s:.*)\w/(.*)', item.url).group(1)

    def run(self):
        """ Iterate through all the user upvoted posts (withting the @LIMIT) and call for download
            if the subreddit matches the given subreddit by the user through the -s argument.
        """
        for item in self.upvoted:
            #pprint.pprint(vars(item))
            self.amount_of_upvotes_scanned += 1
            if self.check_download_limit():
                filename = self.get_filename(item)
                self.download(filename, item)
            else:
                break
        print(f'\nDone: {self.download_counter} new images downloaded to {self.path}')

        if self.debug:
            print(f'Amount of upvoted posts scanned: {self.amount_of_upvotes_scanned}')
        return

def main():
    parser = argparse.ArgumentParser(description="Reddit Upvote Downloader by Emanuel Ramirez")
    parser.add_argument_group('Required Arguments')
    parser.add_argument('-debug', '--debug', action='store_true', help="Debug flag", required=False)
    parser.add_argument('-s', type=str, help="subreddit", required=False)
    parser.add_argument('-t', type=str, help="Upvoted or Savedposts?", required=False)
    parser.add_argument('-l', type=int, help="Limit of post to download (default: None)", required=False)
    parser.add_argument('-all', action='store_true', help="Download every user upvoted posts", required=False)
    parser.add_argument('-user', action='store_true', help="Save with post author name in front of file name", required=False)
    args = parser.parse_args()
    downloader = redditUpvoteDownloader(args.s, args.l, args.user, args.debug)
    downloader.run()


if __name__ == '__main__':
    main()
