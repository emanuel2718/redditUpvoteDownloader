[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

<h1 align="center" style="font-size: 3rem;">
Reddit Upvote Downloader
</h1>

*insert some project description here*
Unfortunately, reddit gives a hard limit of 1024 votes to scan. Keep that in mind.

# Installation:

Clone this repo:
```sh
git clone https://github.com/emanuel2718/redditUpvoteDownloader.git
cd redditUpvoteDownloader
```

Intall requirements:
```sh
pip install -r requirements.txt
```

# How to run:

Example: Grab the upvoted images from r/mechanicalkeyboards subreddit with the -s flag
```sh
python3 main.py -s mechanicalkeyboards
```

# TODO:

- [x] make an option to pass the limit as an argument with -l flag
- [ ] make flag -all to download all the upvoted posts no matter the subreddit
- [ ] add the option to save the file with the format: username_posttitle.extension
- [ ] add better error handling
- [ ] add the option of downloading 'saved' videos
- [ ] make instructions to change config.ini.example -> config.in
- [ ] make table for arguments explanations in the README file

