import time
import os
import datetime as dt


os.chdir('/Users/christiankossi/Downloads')
files = os.listdir(os.getcwd())
present_time = time.time()
days = 30*24*60*60
for file_name in files:
   #checking if the item is file or directory
   if not os.path.isdir(file_name):
     #getting last access time of file
     access_time = os.stat(file_name).st_atime
     #checking if the file was accessed within last 30 days
     timestamp = dt.datetime.fromtimestamp(present_time - days)
     access = dt.datetime.fromtimestamp(access_time)
     print(access.strftime('%Y-%m-%d %H:%M:%S'))
     print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
     if access_time < (present_time - days):
       print('hello acc')
       #removing file which is not accessed for last 30 days
       os.remove(file_name)
       print(file_name + ' removed')