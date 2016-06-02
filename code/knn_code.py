import csv
import random
from operator import itemgetter
from math import *

def euclidean_dist(var2, var1,index_class,dimension):
	for x in range(0,dimension):
		if x==0:
			distance=0
		if x==index_class:
			continue
		if var1[x]=='?':
			var1[x]='5'
		if var2[x]=='?':
			var2[x]='5'
		var1[x]=float(var1[x])
		var2[x]=float(var2[x])
		if var1[x]>100000:
			continue	
		temp_power=	pow((var1[x]) - (var2[x]), 2)
		distance = distance + temp_power
	result=sqrt(distance)
	return result

def find_knn(training, test_inst, k,index_class,length):
	distances=[]
	neighbours = []
	for i in range(length):
		result_d=euclidean_dist(training[i],test_inst,index_class,len(test_inst))
		distances.append((training[i], result_d))
	distances.sort(key=itemgetter(1))	
	for i in range(0,k):
		neighbours.append(distances[i][0])
	return neighbours	
	pass


def predict(index_class,neighbours,len_neighbour):
	class_dict = {}
	for i in range(0,len_neighbour):
		pred_clss = neighbours[i][index_class]
		if pred_clss not in class_dict:
			class_dict[pred_clss]=1
		else:
			class_dict[pred_clss]=class_dict[pred_clss]+1
	temp_sort=sorted(class_dict.iteritems(), key=itemgetter(1), reverse=True)	
	class_dict = {}
	return temp_sort[0][0]	


def get_accuracy(test, predictions, index_class):
	correct=0
	for i in range(len(test)):
		temp = predictions[i]
		if test[i][index_class] != temp:
			continue
		elif test[i][index_class] == predictions[i]:
			correct+=1
	accuracy_percentage = (correct/(float(len(test)))) * 100
	return accuracy_percentage

def mean_standard_deviation(accur_per_list):
	sum=0
	diff_sq = 0
	mean_sd=[]
	length = len(accur_per_list)
	for i in range(length):
		sum+=float(accur_per_list[i])

	mean = sum/length
	mean_sd.append(mean)
	for i in range(length):
		diff_sq+= pow((accur_per_list[i] - mean_sd[0]), 2)

	diff_sq = diff_sq/len(accur_per_list)
	sd= sqrt(diff_sq)
	mean_sd.append(sd)
	return mean_sd

def print_confusion_matrix(predictions, actual_classes):
	#Fetching the name of the classes to dictionary and then to the list
	classes={}
	class_list =[]
	for i in range(len(actual_classes)):
		if actual_classes[i] in classes:			
			classes[actual_classes[i]]= 1
		else:
			classes[actual_classes[i]]= 1
	
	for i in classes.keys():
		class_list.append(i)

	#Creating confusion matrix as list -> empty list and hence comparing and increasing the count
	confusion_matrix=[]
	count = 0
	for i in range(len(class_list)):
		for j in range(len(class_list)):
			confusion_matrix.append(0)
	temp = count	
	for i in range(len(actual_classes)):
		for j in range(len(class_list)):
			for k in range(len(class_list)):
				temp1 = class_list[j]
				temp2 = class_list[k]
				if actual_classes[i] == temp1 and predictions[i] == temp2:
					count+=1
					index1 = j*len(class_list)+k
					confusion_matrix[index1]+=1

	#Printing confusion matrix
	index = 0
	clas_indx=0
	for i in range(len(class_list)+1):
		for j in range(len(class_list)+1):
			if i==j==0:
				print '{0:15}'.format(' ') ,
			elif i == 0:
				print '{0:15}'.format(class_list[j-1]) ,
			elif j==0:
				print '{0:15}'.format(class_list[i-1]) ,
			else:
				print '{0:15}'.format(confusion_matrix[index]),
				index+=1
		print '\n'




def main():
	datasetname = raw_input('Enter the dataset filename eg. iris.data:')
	index_class = input('Index of the class in dataset: ')
	k = input('Enter the value of k for knn: ')
	print 'Split Ratio : 0.50 - Random SubSampling'
	print 'Split Ratio : 0.20 - Five Fold Cross Validation'	
	split=input('Enter the split ratio : ')
	mean_record_of_iterations=[]
		
	if split !=.5:
		if split !=.2:
			print "invalid input taking random split .5"
	
	if split==0.5:
		accur_per_list=[]
		for no_of_iterations in range(0,10):
			test_class = []
			test_ver=[]
			with open(datasetname,'rb') as file_dataset:
				lines=csv.reader(file_dataset)
				listing=list(lines)
				training=[]
				test=[]
				random.shuffle(listing)
				for x in range(0, len(listing), 2):
					training.append(listing[x])
				for x in range(1,len(listing),2):
					test.append(listing[x])
					pass
				length=len(training)
				predictions=[]

				for i in range(0,len(test)):
					nbrs = find_knn(training, test[i], k,index_class,length)
					len_neighbour = len(nbrs)
					predicted_output = predict(index_class,nbrs,len_neighbour)
					predictions.append(predicted_output)
			
				accuracy = get_accuracy(test, predictions, index_class)
				accur_per_list.append(accuracy)
			
				for i in range(len(test)):
					test_class.append(test[i][index_class])

				print '------------------------------------------------------------------------'
				print 'ITERATION: #',
				print no_of_iterations+1
				print 'Accuracy: ',
				print accuracy
				print '-------------------------------------------------------------------------'
				print_confusion_matrix(predictions, test_class)
				print '*************************************************************************'
				print	
			
	
		mean_sd = mean_standard_deviation(accur_per_list)
		print 'Mean: ',
		print mean_sd[0]
		print 'Standard Deviation: ',
		print mean_sd[1]

	elif split==0.2:
		for no_of_iterations in range(0,10):
			print '------------------------------------------------------------------------'
			print 'ITERATION: #',
			print no_of_iterations+1		
			accur_per_list=[]	
			start = 0.0
			end = 0.2			
			for sub_iterations in range(0,5):
				test_class = []
				test_ver=[]
				with open(datasetname,'rb') as file_dataset:
					lines=csv.reader(file_dataset)
					listing=list(lines)
					training=[]
					test=[]
					random.shuffle(listing)
					
					start_index = int(len(listing) * start)
					end_index = int(len(listing) * end)
					for x in range(0, len(listing)):
						if(x>=start_index and x<end_index ):
							pass
						else:
							training.append(listing[x])
					for x in range(start_index,end_index):
						test.append(listing[x])
						pass
					length=len(training)
					#print len(training)
					#print len(test)
					#print start_index
					#print end_index
					predictions=[]
					start+=0.2
					end+=0.2
					for i in range(0,len(test)):
						nbrs = find_knn(training, test[i], k,index_class,length)
						len_neighbour = len(nbrs)
						predicted_output = predict(index_class,nbrs,len_neighbour)
						predictions.append(predicted_output)
			
					accuracy = get_accuracy(test, predictions, index_class)
					accur_per_list.append(accuracy)
			
					for i in range(len(test)):
						test_class.append(test[i][index_class])

					print 'Fold #',
					print sub_iterations+1
					print 'Accuracy: ',
					print accuracy
				
			
			print '-------------------------------------------------------------------------'				
			mean_sd = mean_standard_deviation(accur_per_list)
			print 'Mean: ',
			print mean_sd[0]
			print 'Standard Deviation: ',
			print mean_sd[1]
			mean_record_of_iterations.append(mean_sd[0])
			print

		grand_mean_sd=[]
		grand_mean_sd = mean_standard_deviation(mean_record_of_iterations)
		print
		print 'Grand Mean: ',
		print grand_mean_sd[0]
		print 'Grand Standard Deviation: ',
		print grand_mean_sd[1]
		print
		print '-------------------------------------------------------------------------'
		print_confusion_matrix(predictions, test_class)
		print '*************************************************************************'


main()