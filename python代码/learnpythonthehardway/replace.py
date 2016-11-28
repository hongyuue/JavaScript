# -*- coding: utf-8 -*-
import os
import re


# def listFiles(dirPath):

    # fileList=[]

    # for root,dirs,files in os.walk(dirPath):

  # for fileObj in files:

      # fileList.append(os.path.join(root,fileObj))

    # return fileList

#path = "c:\Users\Administrator\Desktop\A-1.txt"
f = open('c:\Users\Administrator\Desktop\A-1.txt',"r+")
all_the_lines = f.readlines()

f.seek(0)

f.truncate()

for line in all_the_lines:
	f.write(line.replace('P01','123'),"")
f.close()

# in __name__ == "__main__":
	# main()
