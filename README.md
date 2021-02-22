[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

<h1 align="center" style="font-size: 3rem;">
Reddit Upvote Downloader
</h1>

This project was originally made for my own purposes only of downloading all my r/Battlestations upvoted images
for ideas on my own build. Saw someone on reddit asking for a simple service like this so I decided to make it public.

*All downlaoded images credit goes to reddit and/or the uploader*

# Installation:


#### 1. Clone this repo:
```sh
git clone https://github.com/emanuel2718/redditUpvoteDownloader.git
cd redditUpvoteDownloader
```

#### 2. Intall requirements:
```sh
pip install -r requirements.txt
```

#### 3. [Create a developer application on reddit](https://www.reddit.com/prefs/apps)

#### 4. Click on Are you a developer? create an app

![PrefsPanel01](https://user-images.githubusercontent.com/55965894/108690386-27288d80-74af-11eb-81a9-a0854ca7304d.png)

#### 5. Fill information and click create app

![AppName02](https://user-images.githubusercontent.com/55965894/108690978-d2394700-74af-11eb-9992-e81f8ba71bd4.png)

#### 6. Reddit developer account example data below (Client_id, Client_secret):

![info03](https://user-images.githubusercontent.com/55965894/108691188-10cf0180-74b0-11eb-84c7-c600ee2440ea.png)


#### 7. In `~/<path to this project>/redditupvotedownloader` change the name of `config.ini.example` to `config.ini`

#### 8. In `config.ini` change the placeholder vaules.

![config04](https://user-images.githubusercontent.com/55965894/108691226-1fb5b400-74b0-11eb-8ad8-79264181842b.png)


# How to use:

#### Download all the upvoted images without limit
```sh
python3 upvoteDownload.py -all
```

#### Download the last 50 upvoted images
```sh
python3 upvoteDownload.py -all -l 50
```

#### Download all the upvoted images from r/Mechanicalkeyboards
```sh
python3 upvoteDownload.py -s mechanicalkeyboards
```

#### Download all the upvoted images from r/Battlestations with uploader username in front of filename
```sh
python3 upvoteDownload.py -user -s mechanicalkeyboards
```

# TODO:

- [x] make an option to pass the limit as an argument with -l flag
- [x] add the option to save the file with the format: username_posttitle.extension
- [x] make flag -all to download all the upvoted posts no matter the subreddit
- [x] make table for arguments explanations in the README file
- [x] make instructions to change config.ini.example -> config.in
- [ ] add directory flag to specify download directory
- [ ] add tuple list of supported formats (.png, .jpg. .gif). Maybe flag about more extension?
- [ ] add test suite
- [ ] add better error handling
- [ ] refactor item post name to something more relevant
- [ ] add the option of downloading 'saved' videos

