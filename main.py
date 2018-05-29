import re
import os

path = "C:/Users/Kawish/Pictures/iPhotos"

listA = []
allFiles = ""

for path, subdirs, files in os.walk(path):
	for file in files:
		allFiles += file + " "

duplicates = re.findall("\S* \(\d\)\S*", allFiles)

print("Total Duplicates:", len(duplicates))
print(duplicates)