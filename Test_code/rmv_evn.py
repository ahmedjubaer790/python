NmbrList=[2,3,7,8,23,14,56,78,1,9,5]
FinalNmbr=[]

for x in NmbrList:
    if x%2!=0:
        FinalNmbr.append(x)
print('Final Number list is ',sorted(FinalNmbr))