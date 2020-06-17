#!/usr/bin/python3

import boto3
ec2 = boto3.resource('ec2')

try:
	ec2.Instance('i-098a7cf442c135b96').start()
	print("Started EC2 instance with id 'i-098a7cf442c135b96'.")
except Exception as e:
	print(e)
