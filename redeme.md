____________________________________________________________________________________________________________________________________________
Kalpish Singhal
____________________________________________________________________________________________________________________________________________

===============================================================
 Implement K-nearest neighbour (kNN) classifier
===============================================================
The code given is used to implement K-Nearest Neighbours Algorithm:
->In pattern recognition, the k-Nearest Neighbors algorithm (or k-NN for short) is a non-parametric method used for classification and regression.In both cases, the input consists of the k closest training examples in the feature space.
===============================================================
		     Data set Used
===============================================================
# 1 : IRIS DATA SET
# 2 : WINE DATA SET
# 3 : BREAST CANCER - WISCONSIN DATA SET
	
===============================================================
                      INPUT FORMAT
===============================================================
##implementation 
This application implements Knn classifier-Tested on :
1)1nn
2)3nn

## How to run code:-
-> Language used :-Python
-> $ python 201505513_assignment1.py
-> give the desired input

#Plot
-> language used:-python
->$ python Assigment1_plot.py
===============================================================
                      INPUT FORMAT
===============================================================
->"Enter the dataset filename eg. iris.data" name of dataset file
->"Index of the class in dataset:" index of class in dataset eg 4 in iris,0 in wine,10 in BREAST CANCER
->"Enter the value of k for knn:" 1 or 3
->"Split Ratio : 0.50 - Random SubSampling
   Split Ratio : 0.20 - Five Fold Cross Validation
   Enter the split ratio :"input given as 0.2 for five fold cross validation and 0.5 for Random SubSampling



===============================================================
                      OUTPUT FORMAT
===============================================================
ITERATION number: 
Accuracy: 
confusion matrix:
Mean: 
Standard Deviation: 

 
##Assumptions:-
->Missing Attribute Values: The ‘?’ in the missing attributes are replaced by the average value
->plot take iris.data as default data set should be present in the same folder
->The dataset filenames are assumed to be :
	iris.data
	wine.data
	wisconsin.data
-> if invalid spliting ratio is given as input Random SubSampling is taken to be default spliting mechanism
-> tested for k =1 and k =3
-> one of the desired user output according to the input to the program. 

