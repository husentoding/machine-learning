import matplotlib.pyplot as plt
import math
import pandas as pd
import random

def loadFile():
	trainset = pd.read_csv("TrainsetTugas2.txt",header=None,names=["x","y"],delimiter="\t")
	testset = pd.read_csv("TestsetTugas2.txt",header=None,names=["x","y"],delimiter="\t")
	train_data = []
	test_data = []
	for i in range(len(trainset.x)):
		one_line = [trainset.x[i], trainset.y[i]]
		train_data.append(one_line)
	for i in range(len(testset.x)):
		one_line = [testset.x[i], testset.y[i]]
		test_data.append(one_line)

	return train_data, test_data, trainset, testset

def scatter(data, centroid=None):
	for i in data:
		plt.scatter(data.x, data.y, alpha=0.5, s=7)
	if centroid != None:
		# plt.scatter(centroid[0], centroid[1], alpha=1)
		for satu in centroid:
			plt.scatter(satu[0], satu[1], alpha=1, marker='D')
def scatter_clustered(datascatter, data, centroid=None):
	color =["black", "red", "sandybrown", "seagreen", "royalblue", "plum", "coral", "violet", "lightpink"]
	for i in data:
		plt.scatter(i[0][0], i[0][1], color=color[i[1]])
		# print(data[0])
	if centroid != None:
		# plt.scatter(centroid[0], centroid[1], alpha=1)
		for satu in range(len(centroid)):
			# print(centroid[satu][0])
			plt.scatter(centroid[satu][0], centroid[satu][1], s=100, color= color[satu], marker="D")
	plt.show()
			
def euclidean(a, b):
	c = (a[0]-b[0])**2
	d = (a[1]-b[1])**2
	return math.sqrt(c+d)

k = 9
centroid = [[16.169078947368423, 4.613157894736842], [21.47124999999999, 23.16875], [7.490789473684209, 3.9407894736842106], [9.059642857142855, 22.942857142857154], [7.848611111111111, 12.062499999999998], [33.10967741935484, 8.782258064516133], [32.65272727272726, 22.114545454545446], [21.557831325301205, 7.26867469879518], [14.96319444444444, 10.127777777777778]]
data = loadFile()
result = []

for i in data[1]:
	pilih_min = []
	for j in range(len(centroid)):
		a = euclidean(i,centroid[j])
		pilih_min.append(a)
	result.append([i, pilih_min.index(min(pilih_min))])
scatter_clustered(data[3], result, centroid= centroid)
file = open('results_here.txt', 'w')
# print(result)
for i in result:
	file.write(str(i[0][0])+"|")
	file.write(str(i[0][1])+" cluster: ")
	file.write(str(i[1]))
	file.write("\n")
file.close()
print("file write done")

scatter(data[3], centroid= centroid)
