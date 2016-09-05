
#For this program to work, the following packages must be installed.
# sudo python get-pip.py
# Install scikit learn and matplotlib and numpy packages for the program to work
# sudo apt-get install build-essential python3-dev python3-setuptools python3-numpy python3-scipy python3-pip libatlas-dev libatlas3gf-base
# sudo pip3 install scikit-learn
# TO install matplotlib
# sudo apt-get install python-matplotlib
# sudo apt-get install python-numpy

from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import random
f=open('pima-indians-diabetes.data')

lines=sum(1 for line in f)
i=-1
X=np.zeros((lines,9))
rang,variance,dist=np.zeros(9),np.zeros(9),np.zeros(9)
accuracy,avg_acc=np.zeros((6,10)),0


f=open('pima-indians-diabetes.data')
for line in f:
 i=i+1
 pair=line.rstrip().rsplit(',')
 for j in range(0,len(pair),1):
  if len(pair)==9:
   X[i][j]=float(pair[j])
print " Experiment    Accuracy"

for loop in range(0,10,1):
	i=-1
	 
	random.shuffle(X)	#dataset is shuffled
	feature=X[:,:8]		#dataset is split to feature-vector and value
	value=X[:,8:]

	trainX=feature[int(lines*0.9):]	#dataset is split into training and testing 90,10
	testX=feature[:int(lines*0.9)]
	trainY=value[int(lines*0.9):]
	testY=value[:int(lines*0.9)]


	#Support Vector Machines
	clf=svm.SVC()				#classifier model mentioned
	clf.fit(feature,value.ravel())		#classifier built using training data
	
	accuracy[0][loop]=clf.score(testX,testY.ravel())	#classifier mean accuracy predicted using the testing data	
 
	#Linear SVM Kernel
	clf=svm.LinearSVC()
	clf.fit(feature,value.ravel())
	
	accuracy[1][loop]=clf.score(testX,testY.ravel())	
	
	#SVC Radial Basis 
	clf=svm.SVC(kernel='rbf')
	clf.fit(feature,value.ravel())
	
	accuracy[2][loop]=clf.score(testX,testY.ravel())	
	
	#Sigmoid SVM
	clf=svm.SVC(kernel='sigmoid')
	clf.fit(feature,value.ravel())
	
	accuracy[3][loop]=clf.score(testX,testY.ravel())		
	
for i in range(0,4,1):
 for j in range(0,10,1):
  print " ",j+1,"    ",accuracy[i][j]	
 total_acc=sum(value for value in accuracy[i])
 avg_acc+=(total_acc/len(accuracy[0]))*100
 print "Overall Accuracy = ",(total_acc/len(accuracy[0]))*100
print "Average Accuracy=",(avg_acc/400)*100
