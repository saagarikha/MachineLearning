#library(adabag)
library(e1071)
library(rpart)
library(gmodels)
library(class)
library(neuralnet)
library(randomForest)
args <- commandArgs(TRUE)
dataURL<-as.character(args[1])
header<-as.logical(args[2])
d<-read.csv(dataURL,header = header)
d<-na.omit(d)
if (dataURL=='http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wpbc.data')
  d<-d[,-35]
acc<-array(0,9)
set.seed(123)
for(i in 1:10) {
  cat("\nRunning sample ",i,"\n")
  sampleInstances<-sample(1:nrow(d),size = 0.9*nrow(d))
  trainingData<-d[sampleInstances,]
  testData<-d[-sampleInstances,]
  Class<-trainingData[,as.integer(args[3])]
  
  #DECISION TREE
  model_dtree<-rpart(Class~.,method='class',data=trainingData,parms = list (split = 'information'))
  
  
  pred<-predict(model_dtree,testData,type=c("class"))
  
  accuracy<-sum(testData[,as.integer(args[3])]==pred)/nrow(testData)
  acc[1]=acc[1]+accuracy
  cat("\nThe accuracy of decision tree is",accuracy*100)
  
  #SVM
  model_svm<-svm(as.factor(Class)~.,data=trainingData)
  pred_svm<-predict(model_svm,testData)
  table_pred<-table(pred_svm,testData[,as.integer(args[3])])
  accuracy<-(table_pred[1]+table_pred[4])/nrow(testData)
  acc[2]=acc[2]+accuracy
  cat("\nThe accuracy of SVM Classifier is:",accuracy*100)
  
  #NAIVE BAYES
  model_naive<-naiveBayes(as.factor(Class)~.,data=trainingData,type=c("class"))
  pred_naive<-predict(model_naive,testData)
  table_pred<-table(pred_naive,testData[,as.integer(args[3])])
  accuracy<-(table_pred[1]+table_pred[4])/nrow(testData)
  cat("\nThe accuracy of NB Classifier is:",accuracy*100)
  acc[3]=acc[3]+accuracy
  
  #Logistic Regression
  mylogit <- glm(Class ~., data = trainingData, family = "binomial",control=list(maxit=50))
  
  p<-predict(mylogit, newdata=testData, type="response",se.fit=FALSE)

  threshold=0.5
  prediction<-sapply(p, FUN=function(x) if (x>threshold) 2 else 1)

  actual<-testData[,as.integer(args[3])]
  actual<-c(actual)
  for(i in 1:length(actual)){ if (actual[i]==0)actual[i]=1 else actual[i]=2 }
  accuracy <- sum(actual==prediction)/length(actual)
  cat("\n The accuracy for Logistic Regression is:",accuracy*100)
  acc[4]=acc[4]+accuracy
  
    
  #knn
  train_data<-sapply(trainingData,as.numeric)
  test_data<-sapply(testData,as.numeric)
  model_knn <-knn(train=train_data[,-2],test=test_data[,-2],cl=Class,k=3)
  table_pred<-table(model_knn,test_data[,as.integer(args[3])])
  accuracy<-(table_pred[1]+table_pred[4])/nrow(test_data)
  cat("\nThe accuracy of KNN Classifier is:",accuracy*100)
  
  acc[5]=acc[5]+accuracy

  #neuralnetwork
  n <- names(trainingData)
  trainingData<-sapply(trainingData,as.numeric)
  testData<-sapply(testData,as.numeric)
  f <- as.formula(paste(colnames(trainingData)[as.integer(args[3])],"~", paste(n[!n %in% colnames(trainingData)[as.integer(args[3])]], collapse = " + ")))
  f1<-paste(c(n[!n %in% colnames(trainingData)[as.integer(args[3])]]))
  creditnet <- neuralnet(f ,trainingData, hidden = 4, threshold = 0.1)
  temp_test <- subset(testData, select = c(f1))
  creditnet.results <- compute(creditnet, temp_test)
  
  results <- data.frame(actual = testData[,as.integer(args[3])], prediction = creditnet.results$net.result)
  results$prediction <- round(results$prediction)
  accuracy<-sum(results[,2]==testData[,as.integer(args[3])])/nrow(testData)
  cat("\n The accuracy for Neural Network is:",accuracy*100)
  acc[6]=acc[6]+accuracy
  
  #RANDOM FOREST
  mod1<-randomForest (factor(Class)~.,data=trainingData,mtype=4,ntree=400)
  pre1<-predict(mod1 , newdata=testData)
  pre1<-c(pre1)
  actual<-testData[,as.integer(args[3])]
  accu_RFor <- sum(actual==pre1)/length(pre1)
  cat("\n Accuracy for Random Forest", accu_RFor*100)  
  acc[7]=acc[7]+accuracy
  
  #BAGGING AND BOOSTING  
  classCol<-as.numeric(args[3])
  classnumber<-classCol
  namesofattr<-names(d)
  f <- as.formula(paste(namesofattr[classnumber],paste(namesofattr[!namesofattr %in% namesofattr[classnumber]],collapse = " + "),sep = " ~ "))
  trainingData$Class<-factor(trainingData$Class)
  adaBoostingModel <- boosting(f, data = trainingData, mfinal = 10, control = rpart.control(maxdepth = 1))
  
  testData$Class<-factor(testData$Class)
  bosstingPredictionModel <- predict.boosting(adaBoostingModel, newdata =testData)
  
  trainingData$Class<-factor(trainingData$Class)
  boostingCVModel <- boosting.cv(f, v = 10, data =trainingData, mfinal = 10, control = rpart.control(maxdepth = 1))
  #BOOSTING ACCURACY
  accuracy<-(boostingCVModel$confusion[1]+boostingCVModel$confusion[4])/nrow(trainingData)
  print(c("The accuracy for boosting is:",(boostingCVModel$confusion[1]+boostingCVModel$confusion[4])/nrow(trainingData)))
  
  acc[8]=acc[8]+accuracy
  # bagging
  trainingData$Class<-factor(trainingData$Class)
  baggingModel <- bagging(f, data = trainingData, mfinal = 10, control = rpart.control(maxdepth = 1))
  testData$Class<-factor(testData$Class)
  
  predictionBaggingModel <- predict.bagging(baggingModel, newdata = testData)
  
  baggingModelcv <- bagging.cv(f, v = 10, data = trainingData, mfinal = 10, control = rpart.control(maxdepth = 1))
  print(c("The accuracy for Bagging is:",(baggingModelcv$confusion[1]+baggingModelcv$confusion[4])/nrow(trainingData)))  
  
  acc[9]=acc[9]+(baggingModelcv$confusion[1]+baggingModelcv$confusion[4])/nrow(trainingData)
}
cat("\n The average accuracy of 10 sampling in order mentioned in question is:")
for(i in 1:9){
  cat("\n Accuracy",(acc[i]/10)*100)
}
