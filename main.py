""" Created by Emanuel Rmairez Alsina"""

import argparse
import configparser
import praw
import pprint

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
        self.user = self.reddit.user.me()
        self.upvoted = self.user.upvoted(limit=1)

        #pprint.pprint(vars(self.upvoted))
        for u in self.upvoted:
            if u.subreddit == 'battlestations':
                print(f'{u.url} - {u.title}')
            #pprint.pprint(vars(u))

            #print(u.url + ' - ' + u.title)



def main():
    parser = argparse.ArgumentParser(description="Reddit Upvote Downloader by Emanuel Ramirez")
    req_args = parser.add_argument_group('Required Arguments')
    req_args = parser.add_argument('-s', type=str, help="subreddit", required=False)
    args = parser.parse_args()
    downloader = redditUpvoteDownloader(args.s)






if __name__ == '__main__':
    main()
