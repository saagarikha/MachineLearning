
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
accuracy,total_acc=np.zeros(10),0


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
	 
	random.shuffle(X)
	feature=X[:,:8]
	value=X[:,8:]

	trainX=feature[int(lines*0.9):]
	testX=feature[:int(lines*0.9)]
	trainY=value[int(lines*0.9):]
	testY=value[:int(lines*0.9)]


	#Multinomial Naive Bayes
	clf = MultinomialNB()
	clf.fit(feature,value.ravel())

	accuracy[loop]=clf.score(testX,testY.ravel())
	
for j in range(0,10,1):
 print " ",j+1,"    ",accuracy[j]	
 total_acc+=accuracy[j]
print "Overall Accuracy = ",(total_acc/len(accuracy))*100
