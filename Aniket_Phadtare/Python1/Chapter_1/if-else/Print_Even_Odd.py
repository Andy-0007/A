a=10
E=[]
O=[]
for i in range(0,a+1):
    if i%2==0:
        E.append(i)
    else:
        O.append(i)
print("Even\n"," \n ".join(map(str,E)))
print("Odd\n"," \n ".join(map(str,O)))
   
     
  
