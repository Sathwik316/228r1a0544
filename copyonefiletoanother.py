fp1=open("cse a1.txt","r")
fp2=open("cse a.txt","r")
if fp1:
    print("File open successfully")
for i in fp1:
    fp2.write(i)
print("File is copied successfully")
cont=fp2.read()
print(cont)
#print(cont)
fp1.close()
fp2.close()