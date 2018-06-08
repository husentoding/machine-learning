from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix

import numpy as np

def load():
	data_test = []
	data_test_target = []
	data_train= []
	data_train_target = []
	with open ('seeds_dataset.txt', 'r') as f:
		for i in f:
			i = i.replace("\n", "")
			i = i.replace("\t\t", "\t")
			i = i.replace("\t\t\t", "\t")
			i = i.split("\t")
			new_line = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
			data_train.append(new_line)
			data_train_target.append(i[7])
	data_test = data_train[:50]
	data_test_target = data_train_target[:50]
	return data_train, data_train_target, data_test, data_test_target


data_train = load()
# Decision Tree Classifier
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(data_train[0], data_train[1])
y_test = data_train[3]
y_pred = clf_entropy.predict(data_train[2])
print(data_train[3])
# print(f1_score(y_test, y_pred, average="macro"))
# print(precision_score(y_test, y_pred, average="macro"))
# print(recall_score(y_test, y_pred, average="macro"))    
# print(clf_entropy.score(data_train[2], data_train[3]))



# data_train = np.matrix(data_train)
# data_train = np.transpose(data_train)

# knn = KNeighborsClassifier(n_neighbors=2)
# knn.fit(data_train[0], data_train[1])
# print(knn.score(data_train[2], data_train[3]))

# print(data_train[0])
# data_train = np.array(data_train)
# a = np.array(data_train[0])
# b = np.array(data_train[1])
# c = np.array(data_train[2])
# d = np.array(data_train[3])

# mNB = MultinomialNB()
# mNB.fit(a, b)
# print(mNB.score(c, d))

