import shutil
import os
count=0
n=0
conv =0.5 #this value will vary for different test cases in the backend
def rewrite_pagerank():
	os.remove("/home/ruchvad/hadoop/pagerank/v")

	source = "/home/ruchvad/hadoop/pagerank/v1"
	destination = "/home/ruchvad/hadoop/pagerank/v"
	dest = shutil.copyfile(source, destination) 



with open("/home/ruchvad/hadoop/pagerank/v") as file1, open("/home/ruchvad/hadoop/pagerank/v1") as file2:
	for line1, line2 in zip(file1, file2):
		count+=1
		old_pagerank=float(line1.split(",")[1])
		new_pagerank=float(line2.split(",")[1])

		if(abs(old_pagerank-new_pagerank) < conv):
			n+=1

	if(n==count):
		print(0)
	else:
		rewrite_pagerank()
		print(1)
