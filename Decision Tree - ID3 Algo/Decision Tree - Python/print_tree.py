level,flag,cpt=0,0,0
tree_print=[]
def printtree(tree,level,value,k):
 global flag
 while k<len(tree):
   if (tree[k]==111 or tree[k]==222) and value==0:
    m=0 if tree[k]==222 else 1
    print ':',m
    value=1
    level=level
    flag=1 #to show that it is in leaf node and right node shud be included
    k=k+1
    continue
   if (tree[k]==111 or tree[k]==222) and value==1:
    m=0 if tree[k]==222 else 1
    if flag==1 or flag==2:
     for i in range(0,level-1,1):
      print '|',
     print tree_print[len(tree_print)-1]['root'],':',1,
    tree_print[len(tree_print)-1]['value']=1
    print ':',m
    level=level-1
    flag=2 #indicating it went to the previous level this level is over
    k=k+1
    continue
   print
   for i in range(0,level,1):
    print '|',
   if flag==0:
    print tree[k],':',value,
    tl=len(tree_print)
#    print 'Before deletion',tree_print
    for i in range(0,tl-1,1):
     if tree_print[i]['level']==level:
      del tree_print[i]
    tree_print.append({'level':level,'root':tree[k],'value':value})
#    print tree_print,"level",level	
    k=k+1
    level=level+1
    continue
   if flag==1:
     print tree_print[len(tree_print)-1]['root'],':',value
     tree_print[len(tree_print)-1]['value']=1
     level=level+1
     flag=0
     value=0
     continue
   if flag==2:
     value=1
     for i in range(len(tree_print)-1,0,-1):
      if tree_print[i]['value']==0:
       break
     print tree_print[i]['root'],':',value
     level=i
     flag=0
     value=0
     continue   
