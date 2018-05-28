import re
import os

path = "C:/Users/Kawish/Pictures/iPhotos"

# direc = os.listdir(path)

# for _ in direc:
# 	print(_)

listA = []

for (dirpath, dirnames, filenames) in os.walk(path):
	listA.append((dirpath, filenames))


# Total Files
sum = int(0)

for _ in listA:
	print(_[0], ' : ', len(_[1]))
	print()
	sum += len(_[1])

print('Total:', sum)


# Finding Duplicates:

PictureString = ''

for _ in listA:
	for nam in _[1]:
		PictureString += nam + " "

dups = re.findall ('\S*\s\(\d\)\S*', PictureString)

for _ in dups:
	print(_)

# print(listA[0][0])

# s = str("")
# for _ in listA[0][1]:
# 	s += _ + " "

# pinges = re.findall ('\S*\(\d\)\S*', s)

# print(pinges)

