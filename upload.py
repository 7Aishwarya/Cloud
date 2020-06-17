#!/usr/bin/python3
import boto3
import os
ec2 = boto3.resource('ec2')

try:
	print("WARNING: Please ensure that your instance is running")
	file_name = input("Enter filename: ")
	ec2_path = input("Enter path where you want to upload a file on ec2 instance: \n(example: ./ or or /home/ubuntu/)\n")
	os.system('scp -i aish.pem {0} ubuntu@54.161.148.20:{1}'.format(file_name,ec2_path))
	
except Exception as e:
	print(e)
