from __future__ import division
import csv
import numpy as np
import math
import print_tree
import validate_1
import sys

X,Y,Y1,X1=[],[],[],[]
tree=[]
tc=csv.reader(open(sys.argv[1]))
for row in tc:
 if row[0]!='XB':
  Y1.append(map(int,row[len(row)-1:]))
  X1.append(map(int,row[:len(row)-1]))

#X= Feature{Examples} Y= Target variable

for sublist in Y1:
    for val in sublist:
        Y.append(val)

for sublist in X1:
  X.append(sublist)

length= len(X[0])

#Computing the entropy
def Entropy(n,p):
 return -(n*math.log(n,2))-(p*math.log(p,2))

#Computing the entorpy and prediciting the next best node based on information gain
def compute_entropy(ET,cn,cp,target,Y,val):
 k=-1
 flag=0
 cn0,cn1,cp0,cp1=np.zeros(length),np.zeros(length),np.zeros(length),np.zeros(length)
 ET0,ET1,IG=np.zeros(length),np.zeros(length),np.zeros(length)
 for row in target:
  k=k+1
  for i in range(0,length,1):
   if row[i]==Y[k]==0 :cn0[i]+=1
   elif row[i]==Y[k]==1: cp1[i]+=1
   elif row[i]==0 and Y[k]==1: cp0[i]+=1 		#Positives and Negatives in each feature examples
   elif row[i]==1 and Y[k]==0: cn1[i]+=1
 for i in range(0,length-1,1):
  if cn0[i]!=0 and cp0[i]!=0:	
   ET0[i]=((cn0[i]+cp0[i])/(cn+cp))*Entropy(cn0[i]/(cn0[i]+cp0[i]), cp0[i]/(cn0[i]+cp0[i])) 
  if cn1[i]!=0 and cp1[i]!=0:
   ET1[i]=((cn1[i]+cp1[i])/(cn+cp))*Entropy(cn1[i]/(cn1[i]+cp1[i]), cp1[i]/(cn1[i]+cp1[i]))
  if cn0[i]==0 or cp0[i]==0: ET0[i]=0			#Entropy computation
  elif cn1[i]==0 or cp1[i]==0 : ET1[i]=0
  elif cn0[i]==0 and cp0[i]==0:
   if cn1[i]>cp1[i]: flag=222 #predicting 0
   else: flag=111 #predicting 1 
   max_info=i
   break
  elif cn1[i]==0 and cp1[i]==0:
   if cn0[i]>cp0[i]: flag=222 #predicting 0
   else: flag=111 #predicting 1 
   max_info=i
   break  
  IG[i]=ET-ET0[i]-ET1[i]
  if IG[i]==ET : 
   if cn>cp: 
    if val==0: flag=222
    else    : flag=111
   if cn<cp:
    if val==0: flag=111
    else : flag=222
 if flag==0: max_info=IG.argmax()
 if flag==222: return 222
 elif flag==111: return 111
 return max_info 
 
#Target examples split based on the feature 
def split(next_node,value,target,y):
 y1,x,cn,cp=[],[],0,0
 k=-1
 for row in target:
  k=k+1
  if row[next_node]==value:
    x.append(row)
    y1.append(y[k])
  if row[next_node]==y[k]==value:cn+=1
  elif row[next_node]==value and y[k]!=value : cp+=1 
 return x,cn,cp,y1

def Build_Tree(ET,node,target,cn,cp,y,val):
 next_node=compute_entropy(ET,cn,cp,target,y,val)	# The next best node to be taken is computed based on information gain
 tree.append(next_node)					# Appending the node to the tree
 if tree[-1]==111 or tree[-1]==222: return		# If its a leaf node, return
 cn,cp=np.zeros(2),np.zeros(2)
 X1,cn[0],cp[0],y1=split(next_node,0,target,y)		# Splitting the target examples based on the feature values
 X2,cn[1],cp[1],y2=split(next_node,1,target,y)
 for i in range(0,2,1):
   if cn[i]==0 :
    tree.append(111) 						# If node is a leaf node, return
    continue
   elif cp[i]==0 : 
    tree.append(222)
    continue
   else:
    ET=Entropy(cn[i]/(cn[i]+cp[i]), cp[i]/(cn[i]+cp[i]))	
    if i==0: Build_Tree(ET,next_node,X1,cn[i],cp[i],y1,i)	#Continuing to build the tree
    if i==1: Build_Tree(ET,next_node,X2,cn[i],cp[i],y2,i)

cn,cp=0,0
for i in range(0,len(Y),1):
 if Y[i]==0:cn+=1
 else: cp+=1

ET=Entropy(cn/(cn+cp),cp/(cn+cp))	# The entropy of Class is computed
Build_Tree(ET,20,X,cn,cp,Y,-1)          # Building the decision tree 
print_tree.printtree(tree,-1,0,0)	# To print the decision tree
validate_1.validate()                   # To validate the decision tree
