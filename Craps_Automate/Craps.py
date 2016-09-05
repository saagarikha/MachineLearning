from random import randint

outf= open('output_MLass1.txt','wt')

def craps_even(bal,bet,pred,j,flag):
 if bal<100 :
  return 0,j,flag
 if pred == 7 or pred==11 and j==1:
  bal=bal+100
 elif pred==7 and j!=1 and flag==0:
  bal=bal-100
  flag=1
 elif bet==pred and j!=1 and flag!=1 :
   bal=bal+100
 elif pred==2 or pred==3 or pred==12 and j==1:
   bal=bal-100
 return bal,j,flag,

def craps_mart(bal,val,bet,pred,wager,j,flag):
 w=2*wager if bal>2*wager else bal
 if pred==7 or pred==11 and j==1:
  bal=bal+wager 
  wager=100 if val==0 else w 
 elif pred==7 and j!=1 and flag==0:
  wager=w if val==0 else 100
  bal=bal-wager
  flag=1
 elif bet==pred and j!=1 and flag!=1 :
  bal=bal+wager 
  wager=100 if val==0 else w
 elif  pred==2 or pred==3 or pred==12 and j==1:
   wager=w if val==0 else 100
   bal=bal-wager
 return bal,wager,j,flag  

die_val=[]
tot=[0,0,0]
hig={'0':'Even Wager','1' : 'Martingale System', '2':'Reverse Martingale'}
for i in range(1,6):
 bal=[1000,1000,1000]
 wager=[100,100,100]
 game=[0,0,0]
 flag=[0,0,0]
 die_val=[randint(1,6),randint(1,6)] 
 die_sum=die_val[0]+die_val[1]
 bet=[die_sum,die_sum,die_sum] 
 op=""
 for j in range(1,11):
  die_val=[randint(1,6),randint(1,6)] 
  die_sum=die_val[0]+die_val[1]
  bal[0],game[0],flag[0]=craps_even(bal[0],bet[0],die_sum,j,flag[0])
  if bal[1]>=100:
    bal[1],wager[1],game[1],flag[1]=craps_mart(bal[1],0,bet[1],die_sum,wager[1],j,flag[1])
  if bal[2]>=100:
    bal[2],wager[2],game[2],flag[2]=craps_mart(bal[2],1,bet[2],die_sum,wager[2],j,flag[2])
 outf.write("Round :"+str(i)+"\n    Stratergy 1    "+str(bal[0])+"  Games  "+str(game[0])+"\n    Stratergy 2    "+str(bal[1])+"    Games   "+str(game[1])+"\n    Stratergy 3   "+str(bal[2])+"   Games   "+str(game[2]))
 outf.write('\n')
 tot[0],tot[1],tot[2]=tot[0]+bal[0], tot[1]+bal[1], tot[2]+bal[2]
high= 0 if tot[0]>tot[1] else 1
high1= tot[0] if tot[0]>tot[1] else tot[1]
high=2 if tot[2]>high1 else high
outf.write("The best stratergy that worked is : " + hig[str(high)]) 
