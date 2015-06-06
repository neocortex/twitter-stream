twitter-stream
==============

A Twitter stream listener based on [tweepy](http://www.tweepy.org/) that stores received tweets in a mongoDB database.


### Depedencies

- [mongoDB](https://www.mongodb.org/)
- [pymongo](https://pypi.python.org/pypi/pymongo/)
- [tweepy](http://www.tweepy.org/)

### Usage

Specify the terms to be tracked at the bottom of ``stream.py`` and run:

``python stream.py``
