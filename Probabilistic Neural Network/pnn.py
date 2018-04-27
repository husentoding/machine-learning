import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

#asumsi pengerjaan
#data 1-100 training
#data 101-150 validasi

#important variables
omega_lul= 0.0091
jumlah_kelas = 3



#buka file
def openFileTest():
	count =0
	with open('data_train_PNN.csv', 'rb') as csvfile:
		data_x = []
		data_y = []
		data_z = []
		data_class = []
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			a = row[0].split(',')
			data_x.append(a[0])
			data_y.append(a[1])	
			data_z.append(a[2])
			data_class.append(a[3])
			count +=1

	return data_x, data_y, data_z, data_class, count
#buka file test
def openFileTest2():
	count =0
	with open('data_test_PNN.csv', 'rb') as csvfile:
		data_x = []
		data_y = []
		data_z = []
		data_class = []
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			a = row[0].split(',')
			data_x.append(a[0])
			data_y.append(a[1])
			data_z.append(a[2])
			count +=1

	return data_x, data_y, data_z, data_class, count	
# visualisasi data
def showScatter(a,b,c,d):
	fig = plt.figure()
	ax = Axes3D(fig)

	for i in range(0, len(a)):
		x= float(a[i])
		y= float(b[i])
		z= float(c[i])
		if (float(d[i]) == 1):
			ax.scatter(x, y, z, color="r")
		elif (float(d[i])==2):
			ax.scatter(x, y, z, color="g")
		else:
			ax.scatter(x, y, z, color="b")
	plt.show()
#kelompokin data readme
def splitDataIntoClass(a,b,c,d, k, n):
	class_a = []
	class_b = []
	class_c = []
	for i in range(k, n):
		one_row = [a[i], b[i], c[i]]
		# print(float(d[i]))
		if(float(d[i]) == 0):
			class_a.append(one_row)
		elif (float(d[i]) == 1):
			class_b.append(one_row)
		elif (float(d[i]) ==2):
			class_c.append(one_row)
	return class_a, class_b, class_c

#fungsi pdf ini hanya menghitung per kelas
def pdf(omega_lul, x1, x2, x3, xk1, xk2, xk3):
	#xk itu data train
	dalem_exponen = ((x1-xk1)**2)+((x2-xk2)**2)
	pembagi = (2*(omega_lul**2))
	try:
		result = math.exp(-dalem_exponen/pembagi)
	except OverflowError:
		result = float('inf')
	return result

def showGraph(a):
	plt.plot(a)
	plt.show()
prediksi = open("prediksi.txt", "w")
data_lengkap = openFileTest() #data training
data_test = openFileTest2()

#pilah data training
#data training
data_training_x = []
data_training_y = []
data_training_z = []
data_training_class = []
for i in range(0, 100):
	data_training_x.append(data_lengkap[0][i])
	data_training_y.append(data_lengkap[1][i])
	data_training_z.append(data_lengkap[2][i])
	data_training_class.append(data_lengkap[3][i])


#pilah data untku validasi atau testing
data_validasi_x = []
data_validasi_y = []
data_validasi_z = []
data_validasi_class = []
# print(data_test)

#validasi, matiin ini klo mw testing
# for i in range(100, 150):
# 	data_validasi_x.append(data_lengkap[0][i])
# 	data_validasi_y.append(data_lengkap[1][i])
# 	data_validasi_z.append(data_lengkap[2][i])
# 	data_validasi_class.append(data_lengkap[3][i])

#testing
for i in range(0, len(data_test[0])):
	data_validasi_x.append(data_test[0][i])
	data_validasi_y.append(data_test[1][i])
	data_validasi_z.append(data_test[2][i])

#result split class 0, class 1, class 2
split_training = splitDataIntoClass(data_training_x, data_training_y, data_training_z, data_training_class, 0, len(data_training_y))
# split_validasi = splitDataIntoClass(data_validasi_x, data_validasi_y, data_validasi_z, data_validasi_class, 0, len(data_validasi_y))
count = 0
for i in range(len(data_validasi_x)) :
	sum_kelas = [0, 0, 0]
	#validasi di tes ke kelas NOL 
	for j in range(len(split_training[0])):
		# print("INI", split_training[0][j][0])
		# print(sum_kelas[0])
		sum_kelas[0] += pdf(omega_lul, float(data_validasi_x[i]), float(data_validasi_y[i]), float(data_validasi_z[i]), float(split_training[0][j][0]), float(split_training[0][j][1]), float(split_training[0][j][2]))
		# print(split_training[0][j][1])
	#validasi di tes ke kelas SATU 
	for j in range(len(split_training[1])):
		# print("INI", split_training[1][j][0])
		sum_kelas[1] += pdf(omega_lul, float(data_validasi_x[i]), float(data_validasi_y[i]), float(data_validasi_z[i]), float(split_training[1][j][0]), float(split_training[1][j][1]), float(split_training[1][j][2]))
		# print(split_training[0][j][1])
	#validasi di tes ke kelas DUA 	
	for j in range(len(split_training[2])):
		# print("INI", split_training[2][j][0])
		sum_kelas[2] += pdf(omega_lul, float(data_validasi_x[i]), float(data_validasi_y[i]), float(data_validasi_z[i]), float(split_training[2][j][0]), float(split_training[2][j][1]), float(split_training[2][j][2]))
		# print(split_training[0][j][1])	
	# print("Probability data ke-,", i, sum_kelas[0]/len(split_training[0]))
	# print("Probability data ke-,", i, sum_kelas[1]/len(split_training[1]))
	# print("Probability data ke-,", i, sum_kelas[2]/len(split_training[2]))
	#hitung probability rata2 
	p = sum_kelas[0]/len(split_training[0])
	q = sum_kelas[1]/len(split_training[1])
	r = sum_kelas[2]/len(split_training[2])
	result = [p, q, r]
	#pilih probability terbaik, jadikan kelas data tersebut
	kelas = result.index(max(result))

	# # Nyalain ini klo mw cek validasi
	# if(kelas == int(data_validasi_class[i])):
	# 	count+=1

	#print ke terminal dan tulis ke file
	print(i, result.index(max(result)))
	prediksi.write(str(result.index(max(result))))
	prediksi.write("\n")
# print(count/float(len(data_validasi_x)))



#munculin scatter
showScatter(data_lengkap[0], data_lengkap[1], data_lengkap[2], data_lengkap[3])
