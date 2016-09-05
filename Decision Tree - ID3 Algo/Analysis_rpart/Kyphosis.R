#kyphosis initial tree construction
library(rpart)
attach(kyphosis)
fit<- rpart(Kyphosis~ Age+Number+Start,data=Kyphosis,method="class",parms = list(split = 'information'),minsplit=0) #create decision tree model
print(fit)  
par(mar=rep(0.1,4))
plot(fit) #tree plot
text(fit) #important attributes
summary(fit)

printcp(fit)
pfit <- rpart(Kyphosis ~ ., kyphosis, control = rpart.control(cp = fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"])) #prune params to create pruned tree
par(mar=rep(0.1,4))
plot(pfit) #displaying the pruned decision tree
text(pfit)
summary(pfit)

#dividing the dataset to 80-20
train =kyphosis[1:(nrow(kyphosis)*0.8),]
k<-(nrow(kyphosis)-nrow(kyphosis)*0.8)
test = kyphosis[(nrow(kyphosis)*0.8):nrow(kyphosis),]

#training decision tree using the pruned parameters(best cp value)
fit1<- rpart(Kyphosis~ Age+Number+Start,data=train,method="class",parms = list(split = 'information'),control = rpart.control(cp = fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"]))
print(fit1)  
par(mar=rep(0.1,4)) #printing the trained decision tree
plot(fit1)
text(fit1)
summary(fit1)

pred<-predict(fit1,test,type=c("class"))     #predicting the trained decision tree with test
accuracy<-sum(test$Kyphosis==pred)/length(pred)
print(accuracy) #accuracy computation

#dividing the dataset to 90-10
train =kyphosis[1:(nrow(kyphosis)*0.9),]
print(train)
k<-(nrow(kyphosis)-nrow(kyphosis)*0.9)
test = kyphosis[(nrow(kyphosis)*0.9):nrow(kyphosis),]

#pruned decision tree model using training dataset
fit1<- rpart(Kyphosis~ Age+Number+Start,data=train,method="class",parms = list(split = 'information'),control = rpart.control(cp = fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"]))
print(fit1)  
par(mar=rep(0.1,4))
plot(fit1)  #dont print this ##drawing the decision tree
text(fit1)
summary(fit1)

pred<-predict(fit1,test,type=c("prob")) #predict the accuracy
accuracy<-sum(test$Kyphosis==pred)/length(pred)
print(accuracy) #print the accuracy
