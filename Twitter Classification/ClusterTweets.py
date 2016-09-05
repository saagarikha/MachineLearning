from __future__ import division
from nltk.stem.porter import *
from nltk.corpus import stopwords
import urllib2,json,math,numpy

X,Y,kx,ky,kx_index,sse_index=[],[],[],[],{},{}
it,flag,sse=0,0,0
out=open('Twitter_Results.txt','w')

#jaccard distance computation and not considering retweets
def compute_jaccard(center_text,tweet):
 if len(numpy.where(tweet=="RT")[0])>=1 : return -1
 return 1-(len(set.intersection(*[set(center_text),set(tweet)]))/len(set.union(*[set(center_text),set(tweet)]))) 

def pass_text(point):
 for i in range(len(tweet)):
  if tweet[i]['id']==point:
    return i

#loading the dataset as a json list and initial centroids
tweet,points=[],[]
tweets=urllib2.urlopen('http://www.utdallas.edu/~axn112530/cs6375/assignment5/Tweets.json')
centroid=urllib2.urlopen('http://www.utdallas.edu/~axn112530/cs6375/assignment5/InitialSeeds.txt').read().split(',\n')
ii=0
for line in centroid:
 points.append(int(line))
 sse_index[ii],kx_index[ii],ii=[],[],ii+1	
for line in tweets:
 tweet.append(json.loads(line))

#stopwords and stemming the text of tweet
stop=stopwords.words('english')
stemmer=PorterStemmer()
var=[]
for i in range(len(tweet)):
	stem=""
	for word in tweet[i]['text'].split() :
		if word not in stop :
			stem+=word
			stem+=' '
	var.append(stem)

#compute jaccard distance for initial centroids
while(it<25):
	flag=0
	tmp_x=[]
	for i in range(len(points)) : 
	 del kx_index[i][:] 
	 del sse_index[i][:]
	for j in range(len(tweet)):
	 dist=[]	
	 for i in range(len(points)):
	  index=pass_text(points[i])
	  dist1=compute_jaccard(numpy.array(tweet[index]['text'].split()),numpy.array(tweet[j]['text'].split()))
	  if dist1!=-1 :
           dist.append(dist1)
         if not(not dist):
	  inde=dist.index(min(dist))
	  sse_index[inde].append(math.pow((min(dist)),2))
	  kx_index[inde].append(j)
	for i in range(len(points)-1,-1,-1):
	 if len(kx_index[i])==0 : 
	   flag=len(points)
	   break
	 inde=sse_index[i].index(min(sse_index[i]))
	 tweet_id= tweet[kx_index[i][inde]]['id']
	 flag=flag+1 if abs(min(sse_index[i]))<=0.001 else 0
	 tmp_x.append(tweet_id)

	if flag==len(points) : break
	points=tmp_x
	it=it+1

for i in range(len(points)):
 out.write(str("Cluster"+str(i)+":\n")) 
 for j in range(len(kx_index[i])): out.write(str(str(tweet[kx_index[i][j]]['id'])+"\n"))
 sse+=sum(float(sse_index[i][j]) for j in range(0,len(sse_index[i]),1))	
out.write(str("Sum of squared error for cluster is:"+str(sse)))
out.close()
