import boto3

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='richer-kitten-carousel')

data = open('/static-web/cat0.jpg', 'rb')
s3.Bucket('kittens.richertan.click').put_object(Key='cat0.jpg', Body=data)

data = open('/static-web/cat1.jpg', 'rb')
s3.Bucket('kittens.richertan.click').put_object(Key='cat1.jpg', Body=data)

data = open('/static-web/cat2.jpg', 'rb')
s3.Bucket('kittens.richertan.click').put_object(Key='cat2.jpg', Body=data)

data = open('/static-web/index.html', 'rb')
s3.Bucket('kittens.richertan.click').put_object(Key='index.html', Body=data)