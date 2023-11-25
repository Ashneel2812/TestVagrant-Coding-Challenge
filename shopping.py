leatherwallet=[1100,18,1]
umbrella=[900,12,4]
cigarette=[200,28,3]
honey=[100,0,2]
tot_amt=0
if(leatherwallet[0]>=500):
  leatherwallet[0]=0.95*leatherwallet[0]
if(umbrella[0]>=500):
  umbrella[0]=0.95*umbrella[0]
if(cigarette[0]>=500):
  cigarette[0]=0.95*cigarette[0]
if(honey[0]>=500):
  honey[0]=0.95*honey[0]


cart=[leatherwallet,umbrella,cigarette,honey]
cart1=["leatherwallet","umbrella","cigarette","honey"]
abc=[]

a=0
maxgst=0
for i in cart:
  abc.append(i[0]*i[2]+(i[0]*i[2]*(i[1]/100)))
  if(i[0]*i[2]*(i[1]/100)>maxgst):
    maxgst=i[0]*i[2]*(i[1]/100)
    a+=1
print("The product with maximim GST is ",cart1[a] ,"and the amount is :",maxgst)
#print("Total Amount is :",sum(abc))





