import os
n="aish.txt"
m="/home/ubuntu/"
os.system('scp -i aish.pem {0} ubuntu@54.161.148.20:{1}'.format(n,m))
