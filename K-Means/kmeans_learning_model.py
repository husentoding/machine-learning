import matplotlib.pyplot as plt
import math
import pandas as pd
import random

# random.seed(9001)

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
			# plt.scatter(satu[0], satu[1], alpha=1, marker='D')
			plt.scatter(satu[0], satu[1], alpha=1, marker='D')
	plt.show()
def euclidean(a, b):
	c = (a[0]-b[0])**2
	d = (a[1]-b[1])**2
	return math.sqrt(c+d)
#penghitungan centroid baru, dipanggil di fungsi kmeans
def new_centroid(data, k):
	centroid = []
	#for evewry centroid
	for n in range(k):
		x = 0
		y = 0
		num = 0
		for i in data:
			if i[1] == n:
				x += i[0][0]
				y += i[0][1]
				num +=1
		centroid.append([x/num,y/num])
	return centroid
#fungsi utama
def kmeans(k,centroid, data):
	#for all data
	result = []
	for i in data:
		c_result = []
		#for all centroid
		for c in centroid:
			#count the euclid between centroid and data
			c_result.append(euclidean(c, i))
		#give cluster label to the data
		result.append([i, c_result.index(min(c_result))])
	#done labeling all dat
	#find new centroid value
	# print(c_result)
	return new_centroid(result, k)
#inisialisasi
k = 9
centroid = []
old_centroid = [0,0]
data = loadFile()
for i in range(k):
	#pilih k vector sbg centroid awal dari trainset
	centroid.append(random.choice(data[0]))
print("CENTROID AWAL", centroid)
iteration =0

#main
while True:
	#centroid lama disimpan utk dibandingkan dengan centroid baru
	old_centroid = centroid
	centroid = kmeans(k, centroid, data[0])
	iteration +=1
	print(iteration, centroid)
	#kalau centroid lama dan baru sama, hentikan learning
	if old_centroid == centroid:
		scatter(data[2], centroid=centroid) 
		break

