#!/usr/bin/python3
import boto3
import os
ec2 = boto3.resource('ec2')

menu = ['List EC2 instances', 'Start EC2 instance', 'Validate connection', 'Connect to terminnal', 'Upload a file to your EC2 instance','Download a file from EC2 instance', 'Stop EC2 instance', 'Exit']

for i in range(len(menu)):
	print(i, menu[i])

n = int(input("Enter the number for the task you want to perform:"))

while True:
	print("********************************************************************************************************************")
	if n == 0:
		for instance in ec2.instances.all():
			print("Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(instance.id, instance.platform,instance.instance_type, instance.public_ip_address, instance.image.id, instance.state))
	elif n == 1:
		try:
			ec2.Instance('i-098a7cf442c135b96').start()
			print("Started EC2 instance with id 'i-098a7cf442c135b96'.")
			check = input("Do you want to connect to terminal?(y/n): ")
			if check == 'y'or check == 'Y':
				os.system('ssh -i "aish.pem" ubuntu@54.161.148.20')
		except Exception as e:
			print(e)

	elif n==2:
		os.system('ping 54.161.148.20')
	elif n==3:
		try:
			os.system('ssh -i "aish.pem" ubuntu@54.161.148.20')
		except Exception as e:
			print(e)

	elif n==4:
		try:
			file_name = input("Enter filename: ")
			ec2_path = input("Enter path where you want to upload a file on ec2 instance: (example: ./ or or /home/ubuntu/)")
			os.system('scp -i aish.pem {0} ubuntu@54.161.148.20:{1}'.format(file_name,ec2_path))

		except Exception as e:
			print(e)
	elif n==5:
		try:
			file_name = input("Enter path where you want to download the file: ")
			ec2_path = input("Enter filename of your ec2 instance: (example format: file_name.txt or /home/ubuntu/file_name.txt) ")
			os.system('scp -i aish.pem ubuntu@54.161.148.20:{1} {0}'.format(file_name,ec2_path))

		except Exception as e:
			print(e)
	elif n==6:
		try:
			ec2.Instance('i-098a7cf442c135b96').stop()
			print("Stopped EC2 instance with id 'i-098a7cf442c135b96'.")
		except Exception as e:
			print(e)
	elif n==7:
		break

	print("********************************************************************************************************************\n\n")
	for i in range(len(menu)):
		print(i, menu[i])

	n = int(input("Enter the number for the task you want to perform:"))
		
