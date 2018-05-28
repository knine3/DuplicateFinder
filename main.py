import re
import os

path = "C:/Users/Kawish/Pictures/iPhotos"

# direc = os.listdir(path)

# for _ in direc:
# 	print(_)

listA = []

for (dirpath, dirnames, filenames) in os.walk(path):
	listA.append((dirpath, filenames))


print(len(listA))

sum = int(0)

for _ in listA:
	print(_[0], ' : ', len(_[1]))
	print()
	sum += len(_[1])

print('Total: ', sum)


# print(listA[0][0])

# s = str("")
# for _ in listA[0][1]:
# 	s += _ + " "

# pinges = re.findall ('\S*\(\d\)\S*', s)

# print(pinges)

