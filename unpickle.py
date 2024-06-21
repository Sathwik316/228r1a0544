import pickle
fp=open("pickelfile.txt","wb")
unpickle=pickle.load(fp)
print(unpickle)