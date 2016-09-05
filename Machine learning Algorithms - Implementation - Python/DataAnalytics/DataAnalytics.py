import numpy as np
import random
import matplotlib .pyplot as plt
f=open('pima-indians-diabetes.data')

lines=sum(1 for line in f)
i=-1
X=np.zeros((lines,9))
rang,variance,dist=np.zeros(9),np.zeros(9),np.zeros(9)
accuracy=np.zeros((6,10))
coef,c=np.zeros(9),np.zeros((8,8))

f=open('pima-indians-diabetes.data')
for line in f:
 i=i+1
 pair=line.rstrip().rsplit(',')
 for j in range(0,len(pair),1):
  if len(pair)==9:
   X[i][j]=float(pair[j])

fig = plt.figure()
ax = fig.add_subplot(111)
#Calculating range, variation and distribution
for i in range(0,len(X[0])-1,1):
 rang[i]=np.mean(X[:,i])
 variance[i]=np.var(X[:,i])
 dist[i]=np.std(X[:,i])

N=len(X[0])
ind=np.arange(N)
width=0.4
rects1 = ax.bar(ind, rang, width,
                color='black',
                yerr=dist,
                error_kw=dict(elinewidth=2,ecolor='red'))
# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,max(rang)+100)
ax.set_ylabel('Distribution')
ax.set_title('Distribution of all variables')


plt.show()

#histogram
for j in range(0,len(X[0])-1,1):
 fig=plt.figure()
 ax=fig.add_subplot(111)
 maxbin=np.arange(int(max(X[:,j])))
 ax.hist(X[:,j],maxbin,color='green')
 hist,bin_edges=np.histogram(X[:,j],bins=maxbin)
 ax.set_xlim(min(maxbin),max(maxbin))
 ax.set_ylim(min(hist),max(hist))
 ax.set_title("Histogram for attribute X"+`j+1`)
# plt.show()
 fig.savefig("Histogram for attribute X"+`j+1`+".png")
 #bar plot
 fig,ax=plt.subplots()
 center=(bin_edges[:-1]+bin_edges[1:])/2
 width=0.7*(bin_edges[1]-bin_edges[0])
 ax.bar(center,hist,width=width)
 fig.savefig("Bar plot for variable X"+`j+1`+".png")
 plt.bar(center,hist,align='center',width=width)
# plt.show()
 b=np.corrcoef(X[:,j],X[:,len(X[0])-1])
 coef[j]=b[0][1]
 print "The correlation of attribute X"+`j`+"with class is:",coef[j]

maxcor,k,l=0,0,0
for i in range(0,(len(X[0])-1)/2,1):
 for j in range(i+1,len(X[0])-1,1):
  b=np.corrcoef(X[:,i],X[:,j])
  c[i][j],c[j][i]=b[0][1],b[0][1]
  if(maxcor<b[0][1]) : 
    maxcor,k,l=b[0][1],i,j
  print "The correlation between X"+`i+1`+"and X"+`j+1`+"is :",c[i][j]
print "The maximum correlation is between"+`k`+"and"+`l`+"and the value is:"+maxcor
