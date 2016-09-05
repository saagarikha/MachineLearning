The main of the project is to compare the performance of various classifier algorithms and analyze its efficiency over a wide range of datasets. The classification algorithms which are compared are:
  1. Decision Tree
  2. Support Vector Machines
  3. Naïve Bayesian
  4. kNN
  5. Logistic Regression
  6. Neural Network
  7. Bagging
  8. Random Forest
  9. Boosting 

The wide range of datasets are obtained when executing the program, fetched, pre-processed and sent to each classifier for learning. The datasets over which the comparison is done are:

*  Credit default dataset that is available at: https://gist.github.com/Bart6114/8675941
*  Graduate School admission dataset of UCLA  : http://www.ats.ucla.edu/stat/data/binary.csv
*  Wisconsin Prognostic Breast Cancer (WPBC)  : 
    * Description is here : https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer- wisconsin/wpbc.names
    * Data is here        : http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer- wisconsin/wpbc.data
*  Wisconsin Diagnostic Breast Cancer (WDBC)  :
    * Description is here : https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer- wisconsin/wdbc.names
    * Data is here        : http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer- wisconsin/wdbc.data
* Ionosphere Dataset                          :
    * Description is here : https://archive.ics.uci.edu/ml/machine-learning- databases/ionosphere/ionosphere.names
    * Data is here        : http://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data

The executeAlgorithms script file contains a boolean flag which helps us to identify whether the dataset has a header or not. It also contains the index of Class variable attribute to classify. The training and testing ratio from dataset is 90:10. The psuedo code of the workflow is:

PseudoCode:
  Read the dataset using the command line 
  Load in memory
  
  Repeat 10 times
  	Create random training and test sample using a ratio of 90:10 
  	for each of the classifiers
      Build a model using the training data Predict on the test data
      Calculate accuracy
      Output accuracy on screen
    end for 
  end Repeat

The average accuracy for each dataset for different classifiers is computed and the analysis is performed and computed.
