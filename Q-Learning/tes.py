q = initQ()
# for i in q:
# 	print(i)
print(data)


x = start_x
y = start_y
x = 9
y = 7
data = data.values.tolist()
randomAction(y, x)
# move("right", 0, 7)
m = getMaxQ(x,y)
print("max dari ",x, y, data[y][x], "adalah", m)
print(len(q))
# for i in range(0,n):
# 	while x!=goal_x and y!=goal_y:
computeQ(7,7,"up",-1)