#!/usr/bin/python3
import boto3
import os
ec2 = boto3.resource('ec2')

try:
	print("WARNING: Please ensure that your instance is running")
	file_name = input("Enter path where you want to download the file: ")
	ec2_path = input("Enter filename of your ec2 instance: \n(example format: file_name.txt or /home/ubuntu/file_name.txt)\n ")
	os.system('scp -i aish.pem ubuntu@54.161.148.20:{1} {0}'.format(file_name,ec2_path))
	
except Exception as e:
	print(e)
