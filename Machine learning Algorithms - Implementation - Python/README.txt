This zip file includes files such as :
	Exp_data_analysis.py => Python file for exploratory data analysis of the given dataset
 	Naive_Bayes.py	     => Python file for Naive Bayes Classifier
        SVM.py               => Python file for Support Vector Machine Classifier
        Knn.py               => Python file for K-Nearest neighbors Classifier
	Explanation.txt      => A brief explanation regarding the classifier and the exploratory data analysis
	Histogram and Barplot image files => Distribution of independent variables on the pima dataset
	Dataset => To build and test the classifier

How to run the program :
	Extract the package and goto the extracted folder location in terminal.
	In terminal, if you have the following packages not installed for python, do install them :
		Scikit-learn
		Numpy
		Matplotlib
		pip
	The installation for these are: 
		#For this program to work, the following packages must be installed.
		# sudo python get-pip.py
		# Install scikit learn and matplotlib and numpy packages for the program to work
		# sudo apt-get install build-essential python3-dev python3-setuptools python3-numpy python3-scipy python3-pip libatlas-dev libatlas3gf-base
		# sudo pip3 install scikit-learn
		# TO install matplotlib
		# sudo apt-get install python-matplotlib
		# sudo apt-get install python-numpy
	Run the program from the terminal as:
		python <filename>.py
	The co-relation among the attributes and class,
	The co-relation between the attributes and maximum co-relation
	The accuracy and overall and average accuracy of Naive Bayes, SVM and Knn are computed and displayed accordingly.
	
	fit(key(feature-vector),value) > fits a classifier mentioned accordingly
	score(key(feature-vector),value) > predicts a mean accuracy for the given test data 
