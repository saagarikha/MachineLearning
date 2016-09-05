from __future__ import division
import csv
import math
import sys

def validate_test():
	tree=version1.tree
	level,c,ic,k=0,0,0,0
	print
	valid_set=csv.reader(open('validation_set.csv'))
	for row in valid_set:
	 for i in range(0,len(row),1):
	  k,level=0,0
	  while level<=int(math.sqrt(len(row)))+1:
	   if tree[k]!='C0' and tree[k]!='C1':
	    if row[int(tree[k])]==str(0): k=k*2+1	
	    elif row[int(tree[k])]==str(1): k=k*2+2
	   if (row[len(row)-1]==str(0) and tree[k]=='C0') or (row[len(row)-1]==str(1) and tree[k]=='C1'): c=c+1  
	   elif (row[len(row)-1]==str(0) and tree[k]=='C1') or (row[len(row)-1]==str(1) and tree[k]=='C0'): ic=ic+1
	   level=level+1
	print "The accuracy is:", (c/(c+ic))*100

def validate():
  c,ic=0,0
  valid_set=csv.reader(open(sys.argv[2]))
  for row in valid_set:
   for i in range(0,len(row),1):
    if row[13]==str(0): 
     if row[11]==str(0) and row[len(row)-1]==str(0):
       c+=1
     elif row[11]==str(0) and row[len(row)-1]==str(1):
       ic+=1
     elif row[11]==str(1):
      if row[0]==0:
        if row[7]==str(0) and row[len(row)-1]==str(0):
          c+=1
        if row[7]==str(1) and row[len(row)-1]==str(1):
          c+=1
        else : ic+=1
      elif row[0]==str(1):
        if row[4]==str(1) and row[len(row)-1]==str(1):
          c+=1
        elif row[4]==str(1) and row[len(row)-1]==str(0):
          ic+=1
        elif row[4]==str(0):
          if row[5]==str(0) and row[len(row)-1]==str(0):
           c+=1
          if row[5]==str(1) and row[len(row)-1]==str(1):
           c+=1
          else : ic+=1
    elif row[13]==str(1):
      if row[7]==str(1) and row[len(row)-1]==str(1):
        c+=1
      elif row[7]==str(1) and row[len(row)-1]==str(0):
        ic+=1
      if row[13]==str(1) and row[len(row)-1]==str(1):
        c+=1
      elif row[13]==str(0) and row[len(row)-1]==str(0):
        c+=1
      else: ic+=1
  print "The accuracy is:",(c/(ic+c))*100
