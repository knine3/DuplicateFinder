import re
import os

path = "C:/Users/Kawish/Pictures/iPhotos"

allFiles = ""

for path, subdirs, files in os.walk(path):
	for file in files:
		allFiles += os.path.join(path, file) + "\n"

duplicates = re.findall(r"(\S* \(\d\)\S*)", allFiles)

print("Total Duplicate files:", len(duplicates))

# Total Size
totalSize = float(0)

for _ in duplicates:
	totalSize += os.path.getsize(_)

totalSize = round(totalSize/(1048576*1024), 2)

print("Total Size:", totalSize, "GB")