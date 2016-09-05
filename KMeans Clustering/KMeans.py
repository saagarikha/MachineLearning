from __future__ import division
import urllib2
import sys
import random
import math


X,Y,kx,ky,kx_index,sse_index=[],[],[],[],{},{}
flag,it,sse=0,0,0
out=open('kmeans.txt','w')
#load the data :
target=urllib2.urlopen('http://www.utdallas.edu/~axn112530/cs6375/assignment5/test_data.txt').read().split('\r')
for line in target:
 pair=line.split('\t')
 if pair[0]!='id':
  X.append(float(pair[1]))
  Y.append(float(pair[2]))

#obtain the number of clusters:
K=int(raw_input('Enter the number of Clusters: '))
for i in range(K):
 kx.append(float("%.3f"%random.uniform(min(X),max(X))))
 ky.append(float("%.3f"%random.uniform(min(Y),max(Y))))
 kx_index[i],sse_index[i]=[],[]


while(it<25):
	flag=0
	tmp_x,tmp_y=[],[]
	for i in range(K) : 
	 del kx_index[i][:] 
	 del sse_index[i][:]
	for i in range(0,len(X),1):
	 dist=[]
	 for j in range(0,K,1):
	  dist.append(math.sqrt(math.pow((kx[j]-X[i]),2)+math.pow((ky[j]-Y[i]),2)))
	 inde=dist.index(min(dist))
	 sse_index[inde].append(math.pow(min(dist),2))
	 kx_index[inde].append(i)
	 
	for i in range(K-1,-1,-1):
	 if len(kx_index[i])==0 : 
           flag=K 
	   break
         x=(1/len(kx_index[i]))*sum(float(X[l]) for l in kx_index[i])
	 y=(1/len(kx_index[i]))*sum(float(Y[l]) for l in kx_index[i])
	 flag=flag+1 if abs(kx.pop()-x)<=0.001 and abs(ky.pop()-y)<=0.001 else 0
	 tmp_x.append(x)
	 tmp_y.append(y)

	if flag==K : break
	kx,ky=tmp_x,tmp_y
	it=it+1

for i in range(K):
 out.write(str(str(kx_index[i])+"\n"))
 sse+=sum(float(sse_index[i][j]) for j in range(0,len(sse_index[i]),1))	
out.write(str("Sum of squared error for cluster is:"+str(sse)))
out.close()
