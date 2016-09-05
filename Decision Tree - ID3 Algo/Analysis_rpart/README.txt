Files Included :
 Solder.R        = Decision Tree for Solder Dataset in Rpart
 Kyphosis.R      = Decision Tree for Kyphosis Dataset in Rpart

To execute and run the code :
In Linux enviroinment :
 > Extract Analysis_rpart and place them in the desired folder.
 > Goto the desired folder and double click the file and open in Rstudio
 > Execute the sequence of commands to print the decision tree for the dataset.
 > Model using the rpart function is created using the "rpart" function
    which accepts => 1. The outcome and the attributes which affect the outcome
                     2. Dataset for which outcome should be predicted
		     3. Parameter based on which the dataset is classified
                     4. The learning method = (Class = classification, anova = Regression)
 > printcp -> To print the complexity parameter table for the decision tree.
 > plot -> To plot the decision tree.
 > predict -> To predict the test file outcome comparing with the decision tree created using rpart.
              It provides the output predicted for every data in the test file as an array.
 > Accuracy is computed by comparing the outcome predicted using the 'predict' function with the
       outcome in test file and accuracy is computed.
 > complexity parameter (cp) > This is used to prune the tree for higher accuracy to avoid over-fitting of the data.
 


