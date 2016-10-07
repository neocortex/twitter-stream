FROM python:3.5-alpine

RUN pip3 install boto3 tweepy

ADD . /workdir
WORKDIR /workdir

CMD ["python3", "./dynamo_stream_listener.py"]
