#install.packages("rpart", dependencies = TRUE)
library(rpart)

#Decision Tree Creation
train_set1<-read.csv("training_set.csv")
str(train_set1)
fit<- rpart(Class~.,data = train_set1,parms = list (split = 'information'), method = "class",minsplit = 0)
train_set1$variable.importance
print(fit)
plot(fit,uniform=TRUE, main="Decision Tree for dataset1")
text(fit,pretty=0,cex=.7)
summary(fit)
printcp(fit)

#Predicting the tree and calculating accuracy before pruning
file2<-read.csv("test_set.csv")
pred<-predict(fit,file2,type=c("class"))
print(pred)
accuracy<-sum(file2$Class==pred)/length(pred)
print("The accuracy before pruning")
print(accuracy*100)

#Pruning
cpp<- fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"]
print(cpp)
pfit<-rpart(Class~.,data=train_set1,parms = list(split = 'information'),method="class",
            control = rpart.control(cp =0.02))
plot(pfit,uniform=TRUE, main="Post Pruning the Tree set1")
text(pfit,use.n=TRUE, all=TRUE, cex=.7)

#Predicting the tree and calculating accuracy after pruning
file2<-read.csv("test_set.csv")
pred<-predict(pfit,file2,type=c("class"))
print(pred)
accuracy<-sum(file2$Class==pred)/length(pred)
print("Accuracy after pruning")
print(accuracy*100)


#Merging Dataset 1 and Dataset 2
dataset2<-read.csv("training_set2.csv")
mydata <- rbind(file1, dataset2)
str(mydata)
mydatafit<- rpart(Class~.,data = mydata,parms = list (split = 'information'), method = "class",minsplit = 0)
mydatafit$variable.importance
print(mydatafit)
plot(mydatafit,uniform=TRUE, main="Decision Tree after merging the two datasets")
text(mydatafit,pretty=0,cex=.7)
summary(mydatafit)
printcp(mydatafit)

#Predicting the tree and calculating accuracy before pruning and merging dataset
file2<-read.csv("test_set.csv")
testdataset2<-read.csv("test_set2.csv")
testmydata <- rbind(file2, testdataset2)
pred<-predict(mydatafit,testmydata,type=c("class"))
print(pred)
accuracy<-sum(testmydata$Class==pred)/length(pred)
print("Accuracy before pruning and merging two datasets")
print(accuracy*100)


#Post Pruning
cpp<- mydatafit$cptable[which.min(mydatafit$cptable[,"xerror"]),"CP"]
print(cpp)
pfit<-rpart(Class~.,data=mydata,parms = list(split = 'information'),method="class",
            control = rpart.control(cp =0.02))
plot(pfit,uniform=TRUE, main="Post Pruning the Merged Tree set")
text(pfit,use.n=TRUE, all=TRUE, cex=.7)

#Predicting the tree and calculating accuracy after pruning and merging
file2<-read.csv("test_set.csv")
testdataset2<-read.csv("test_set2.csv")
testmydata <- rbind(file2, testdataset2)
str(testmydata)
pred<-predict(pfit,testmydata,type=c("class"))
print(pred)
accuracy<-sum(testmydata$Class==pred)/length(pred)
print("Accuracy after pruning and merging the dataset")
print(accuracy*100)

