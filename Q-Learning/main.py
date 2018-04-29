import pandas as pd
import random

start_x, start_y = 0, 9
goal_x, goal_y = 9, 0
n= 20
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

def bestAction(y, x, prev_x, prev_y, current_reward):
	# print(x, y)
	# print("PREV", prev_x, prev_y)
	value = []; x_result = []; y_result = [];
	global q; global previous_x; global previous_y;
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
		if(a[0] in previous_x and a[1] in previous_y):
			continue
		else:
			"gak"
		s = str(x)+"|"+str(y)
		value.append(q[s][i])
		x_result.append(a[0])
		y_result.append(a[1])
		# print "Pilihan", i, data[a[1]][a[0]]
	index_max = value.index(max(value))
	previous_x.append(x_result[index_max])
	previous_y.append(y_result[index_max])
	# print x_result[index_max], "|", x_result[index_max]
	# print(action[index_max])
	# print("Current reward: ", current_reward)
	key = str(x_result[index_max])+"|"+str(y_result[index_max])
	return x_result[index_max], y_result[index_max], action[index_max], current_reward+q[key][action[index_max]]

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
	global q
	while x != goal_x and y != goal_y:
		#Select one among all possible actions for the current state.
		aksi = randomAction(y, x)
		#Using this possible action, consider going to the next state.
		#Get maximum Q value for this next state based on all possible actions.
		max_q = getMaxQ(x, y)
		# if(x==0 and y == 9):
		# 	print q["0|9"]
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
	current_reward = 0
	# print(x,y, data[y][x])
	global goal_y, goal_x
	prev_x = 0; prev_y = 0;
	while x != goal_x and y != goal_y:
		x, y, aksi, current_reward = bestAction(y, x, prev_x, prev_y, current_reward)
		prev_x = x; prev_y = y;
		# print "masih"
		print x,y
	print "Total reward to reach goal: ", current_reward

q = initQ()
x = start_x
y = start_y
previous_x = []
previous_y = []
print(data)
data = data.values.tolist()
# learn
for i in range(0, n):
	satuEpisode(x, y)
# write in a file
file = open('results.txt', 'w')
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
#to print the q matrix
# printQ(q)


findBestRoute(x, y)