import matplotlib.pyplot as py 

index=0
preindex=0

j=0.5
lists=[]
decision_line_x=[]
decision_line_y=[]
f = open('iris.data', 'rb')
dataset = f.readlines()
 # petal width
xcord3 = []
ycord3 = []
for i in range(len(dataset)):
	test=[]
 	test = dataset[i].split(',')
 	length=len(lists)
 	lists.insert(length,test)
y = 3
x = 1 

xcord1 = []
ycord1 = [] 	
xcord2 = []
ycord2 = []
matrix, labels=[map(float, l[:4]) for l in lists], [l[-1] for l in lists]
#Locating x and y coordinates of the points given ( sepal width and petal width)
for n, elem in enumerate(matrix):
	if labels[n] == 'Iris-setosa\n' and labels[n]!='':
		xcord1.insert(len(xcord1),matrix[n][x])
		ycord1.insert(len(ycord1),matrix[n][y])
	if labels[n] == 'Iris-versicolor\n' and labels[n]!='':
		xcord2.insert(len(xcord2),matrix[n][x])
		ycord2.insert(len(ycord2),matrix[n][y])
	if labels[n] == 'Iris-virginica\n' and labels[n]!='':
		xcord3.insert(len(xcord3),matrix[n][x])
		ycord3.insert(len(ycord3),matrix[n][y])
i=1.5
j=0	
ax = py.figure().add_subplot(111)	
while i<=4.9:
	while j<3:
		preindex=index
		max_value=10000000
		for k in range(0,150):
			if max_value>pow(matrix[k][1]-i,2)+pow(matrix[k][3]-j,2):
				max_value=pow(matrix[k][1]-i,2)+pow(matrix[k][3]-j,2)
				if labels[k]=='Iris-setosa\n':
					index=1
				if labels[k]=='Iris-versicolor\n':
					index=2
				if labels[k]=='Iris-virginica\n':
					index=3
				else:
					pass
		if preindex ==index:
			pass
		else:
			length_line=len(decision_line_x)
			decision_line_x.insert(length_line,i)
			decision_line_y.insert(length_line,j)
		j+=0.1
	j=0	
	i+=0.1		
ax.scatter(decision_line_x, decision_line_y, 10, color ='grey')
ax.set_title('2-D Plot_Iris dataset', fontsize=16)
ax.set_xlabel('Sepal Width (cm)')
ax.set_ylabel('Petal width (cm)')
ax.legend([ax.scatter(xcord1, ycord1, s=40, c='red'), ax.scatter(xcord2, ycord2, s=40, c='green'), ax.scatter(xcord3, ycord3, s=40, c='blue')], ["Iris Setosa", "Iris Versicolor", "Iris Virginica"], loc=2)
ax.grid(True,linestyle='-',color='0.75')	
py.show()
