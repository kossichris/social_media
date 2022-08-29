import os

os.chdir('/Users/christiankossi/Downloads')
files = os.listdir(os.getcwd())

for file_name in files:
 #checking if item is not directory
  if not os.path.isdir(file_name):
    #checking if file is pdf
    if file_name.endswith('.pdf'):
      print(file_name)
      #checking if pdf directory does not exist
      if not os.path.isdir('pdf'):
        #creating pdf directory using system command
        os.system('mkdir pdf')
      #moving pdf file to pdf directory using system command
      os.system('mv '+file_name+' ./pdf/')
    #checking if file is png
    elif file_name.endswith('.png'):
      #checking if images directory exists
      if not os.path.isdir('images'):
        #creating images directory using system command
        os.system('mkdir images')
      #moving png file to images folder using system command
      os.system('mv '+file_name+' ./images/')