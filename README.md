[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

<h1 align="center" style="font-size: 3rem;">
Reddit Upvote Downloader
</h1>

This project was originally made for my own use only. The intent was to automate the download of all my r/Battlestations upvoted images for ideas on my own build. But saw someone on reddit asking for a service like this so I decided to make it public.


*All downlaoded images credit goes to reddit and/or the uploader*



# Index

* [Installation](#installation)
* [How to use](#how-to-use)

# Installation:


#### 1. Clone this repo:
```sh
$ git clone https://github.com/emanuel2718/redditUpvoteDownloader.git
$ cd redditUpvoteDownloader
```

#### 2. Intall requirements:
```sh
$ pip install -r requirements.txt
```

&nbsp; 

#### 3. Change the name of `config.ini.example`
```sh
$ mv config.ini.example config.ini
```

&nbsp; 

#### 4. [Create a developer application on reddit](https://www.reddit.com/prefs/apps)

&nbsp; 

#### 5. Click on `Are you a developer? create an app`

![PrefsPanel01](https://user-images.githubusercontent.com/55965894/108690386-27288d80-74af-11eb-81a9-a0854ca7304d.png)

&nbsp; 

#### 6. Fill information and click `create app`

![AppName02](https://user-images.githubusercontent.com/55965894/108690978-d2394700-74af-11eb-9992-e81f8ba71bd4.png)

&nbsp; 

#### 7. Reddit developer account example data below (Client_id, Client_secret):

![info03](https://user-images.githubusercontent.com/55965894/108691188-10cf0180-74b0-11eb-84c7-c600ee2440ea.png)

&nbsp; 

#### 8. In `config.ini` change the placeholder vaules.

&nbsp; 

# How to use:

#### Download all the upvoted images without limit
```sh
$ python3 upvoteDownload.py -all
```
&nbsp; 

#### Download the last 50 upvoted images
```sh
$ python3 upvoteDownload.py -all -l 50
```
&nbsp; 

#### Download all the upvoted images from r/Mechanicalkeyboards
```sh
$ python3 upvoteDownload.py -s mechanicalkeyboards
```
&nbsp; 

#### Download all the upvoted images from r/Battlestations with uploader username in front of filename
```sh
$ python3 upvoteDownload.py -user -s mechanicalkeyboards
```
&nbsp; 


#### Save upvoted media on given path as ~/Pictures/reddit/subreddit/mechanicalkeyboards/image.ext
```sh
$ python3 upvoteDownload.py --path ~/Pictures --subreddit mechanicalkeyboards
```
&nbsp; 
