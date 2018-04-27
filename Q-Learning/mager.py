import pandas as pd
import random

start_x, start_y = 0, 9
goal_x, goal_y = 9, 0
n= 100
data = pd.read_csv("DataTugasML3.txt", sep=",", header=None);
gamma = 0.8

def move(aksi, x, y):
	global data
	if aksi=="up":
		y-=1
	if aksi=="down":
		y+=1
	if aksi=="left":
		x-=1
	if aksi=="right":
		x+=1
	return x,y

def bestAction(y, x):
	print(x, y)
	value = []; x_result = []; y_result = [];
	global q
	action = ["up", "down", "left", "right"]
	if(x==0):
		action.remove("left")
	if(x==9):
		action.remove("right")
	if(y==0):
		action.remove("up")
	if(y==9):
		action.remove("down")
	for i in action:
		a = move(i, x, y)
		s = str(x)+"|"+str(y)
		value.append(q[s][i])
		x_result.append(a[0])
		y_result.append(a[1])
		# print "Pilihan", i, data[a[1]][a[0]]
	index_max = value.index(max(value))
	return x_result[index_max], y_result[index_max], action[index_max]

def randomAction(y, x):
	action = ["up", "down", "left", "right"]
	global data
	if(x==0):
		action.remove("left")
	if(x==9):
		action.remove("right")
	if(y==0):
		action.remove("up")
	if(y==9):
		action.remove("down")
	aksi = random.choice(action)
	return aksi

def getMaxQ(x,y):
	global data
	action = ["up", "down", "left", "right"]
	if(x==0):
		action.remove("left")
	if(x==9):
		action.remove("right")
	if(y==0):
		action.remove("up")
	if(y==9):
		action.remove("down")
	value = []
	for i in action:
		a = move(i,x,y)
		value.append(data[a[1]][a[0]])
	return max(value)

def computeQ(current_x, current_y, aksi, maks):
	#aksi 0 = left #aksi 1 = right 
	#aksi 2 = up   #aksi 3 = down 
	global gamma
	global q
	key = str(current_x)+"|"+str(current_y)
	next = move(aksi, current_x, current_y)
	# q[key][aksi] = data[next[1]][next[0]] + gamma * maks
	q[key][aksi] = q[key][aksi] + gamma * maks
	# print("value", data[next[1]][next[0]])
	# print("key", key, "aksi", aksi)
	# print(q[key][aksi])

def satuEpisode(x, y):
	global goal_x, goal_y
	while x != goal_x and y != goal_y:
		#Select one among all possible actions for the current state.
		aksi = randomAction(y, x)
		#Using this possible action, consider going to the next state.
		#Get maximum Q value for this next state based on all possible actions.
		max_q = getMaxQ(x, y)
		#Compute: Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
		computeQ(x, y, aksi, max_q)
		#Set the next state as the current state.
		x, y = move(aksi, x, y)
		# print(x,y, aksi)

def initQ():
	q = {}
	for i in range(0,10):
		for j in range(0,10):
			s = str(i)+"|"+str(j)
			q[s] = {}
			q[s]["up"] = 0
			q[s]["left"] = 0
			q[s]["right"] = 0
			q[s]["down"] = 0
	return q

def printQ(q):
	keylist = q.keys()
	keylist.sort()
	for k in keylist:
		print "%s: %s" % (k, q[k])

def findBestRoute(x, y):
	global data
	print(x,y, data[y][x])
	global goal_y, goal_x
	while x != goal_x and y != goal_y:
		x, y, aksi = bestAction(y, x)

q = initQ()
x = start_x
y = start_y
print(data)
data = data.values.tolist()
# learn
for i in range(0, n):
	satuEpisode(x, y)
# write in a file
file = open('results,txt', 'w')
for key in q:
	t = key+"\t"
	s = ""
	for key2 in q[key]:
		s += str(key2)+str(q[key][key2])+"\t"
	file.write(t)
	file.write(s)
	file.write("\n")

# find best route
x = start_x
y = start_y
# print(data[x][y])
findBestRoute(x, y)