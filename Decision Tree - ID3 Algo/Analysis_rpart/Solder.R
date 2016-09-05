#Solder initial tree construction
library(rpart)
attach(kyphosis)
fit <- rpart(Solder ~ Opening + skips + Mask + PadType + Panel,data = solder, method = "class")#create decision tree model
par(mar=rep(0.2,4))
printcp(fit) # display the results
plotcp(fit,main="Classification Tree for Solder") # visualize cross-validation results
text(fit)
summary(fit) # detailed summary of splits

printcp(fit)
pfit <- rpart(Solder ~ Opening + skips + Mask + PadType + Panel, solder, control = rpart.control(cp = fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"])) #prune params to create pruned tree
par(mar=rep(0.2,4))
plotcp(pfit,main="Pruned Classification Tree for Solder") #displaying the pruned decision tree
text(pfit)
summary(pfit)

train =solder[1:(nrow(solder)*0.8),]
k<-(nrow(solder)-nrow(solder)*0.8)
test = solder[(nrow(solder)*0.8):nrow(solder),]

#training decision tree using the pruned parameters(best cp value)
fit1<- rpart(Solder ~ Opening + skips + Mask + PadType + Panel,data=train,method="class",control = rpart.control(cp = fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"]))
printcp(fit1)  
par(mar=rep(0.2,4)) #printing the trained decision tree
plotcp(fit1,main="Pruned 80% Classification decision tree for Solder")
text(fit1)
summary(fit1)

pred<-predict(fit1,test,type=c("class")) #predicting the trained decision tree with test
accuracy<-sum(test$Solder==pred)/length(pred)
print(accuracy) #accuracy computation

#dividing the dataset to 90,10%
train =solder[1:(nrow(solder)*0.9),]
k<-(nrow(solder)-nrow(solder)*0.9)
test = solder[(nrow(solder)*0.9):nrow(solder),]

#pruned decision tree model using training dataset
fit1<- rpart(Solder ~ Opening + skips + Mask + PadType + Panel,data=train,method="class",control = rpart.control(cp = fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"]))
print(fit1)  
par(mar=rep(0.2,4))
plotcp(fit1,main="Pruned 90% Classification Tree for solder")  #Decision Tree
text(fit1)
summary(fit1)

pred<-predict(fit1,test,type=c("class")) #predict the accuracy
accuracy<-sum(test$Solder==pred)/length(pred)
print(accuracy) #print the accuracy 
