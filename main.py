""" Created by Emanuel Rmairez Alsina"""

import argparse
import configparser
import praw

class redditUpvoteDownloader:
    def __init__(self, sub):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.sub = sub
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                            client_secret=config['REDDIT']['client_secret'],
                            user_agent="reddit Upvote Downloader",
                            username=config['REDDIT']['username'],
                            password=config['REDDIT']['password'])
        print(self.reddit.user.me())

def main():
    parser = argparse.ArgumentParser(description="Reddit Upvote Downloader by Emanuel Ramirez")
    req_args = parser.add_argument_group('Required Arguments')
    req_args = parser.add_argument('-s', type=str, help="subreddit", required=False)
    args = parser.parse_args()
    downloader = redditUpvoteDownloader(args.s)






if __name__ == '__main__':
    main()
