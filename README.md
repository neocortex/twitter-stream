twitter-stream
==============

A Twitter stream listener based on [tweepy](http://www.tweepy.org/) that stores received tweets in a DynamoDB/mongoDB database.


### Depedencies

- [boto3](https://boto3.readthedocs.io/en/latest/)
- [pymongo](https://pypi.python.org/pypi/pymongo/)
- [tweepy](http://www.tweepy.org/)

### Usage

Specify the desired list of terms in `dynamo_stream_listener.py`.

Use the attached `Dockerfile` or run the Python executable directly:

    python dynamo_stream_listener.py
