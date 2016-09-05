Files Included :
  decision_tree.py -> Python file for building the decision tree
  print_tree.py -> Python file for printing the decision tree
  validate_1.py -> Python file for validating the decision tree
  
  Dtree.R-> R File for building, pruning, validating and printing the decision tree 
  DTree.pdf -> Image file of building the decision tree
  Dtree_merge.pdf -> Image file of decision tree after merging training_set and training_set2
  Postprune_1.pdf -> Image file of pruned decision tree
  Postprune_merged.pdf ->  Image file of pruned decision tree after merging training_set and training_set2

To execute and run the code for Python:
In Linux environment:
 > Extract the folder Decision_tree and place them in the desired location
 > Goto the location through terminal and in terminal type:
     python decision_tree.py <training_set> <test_set>
        <training_set> = training_set.csv or training_set2.csv
        <test_set>     = test_set.csv or test_set2.csv
 > Accuracy computed and obtained is 58.8%
 > Check the comments in source code for logic of decision tree.


To execute and run the code for R:
In Linux environment :
 > Extract Decison_tree and place them in the desired folder.
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
 

