import os
import random
import time

try:
	import exclude
except:
	file = open("exclude.py","a")
	file.write("# In this python file add files to exclude\n")
	file.write("# Please add a , as a seperator\n")
	file.write("# Steam game shortcuts are .url and others are usually .ink\n")
	file.write("# You need include filetype when adding exceptions\n")
	file.write(f'exceptions = ["exclude.py"]')
	file.close()
	import exclude

if __name__ == "__main__":
	seed = time.time()*6639001/8973580
	print("Seed : "+str(seed))
	random.seed(seed)
	dirlist = os.listdir()
	usable_items = [item for item in dirlist if item not in exclude.exceptions]
	item = (usable_items[random.randint(0, len(usable_items)-1)])
	print("Chose",item,"\nLaunching...")
	os.system('start "" "'+item+'"')