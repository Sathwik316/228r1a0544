import pickle
fp=open("picklefile.txt","wb")
cn=["dhoni","virat","dhavan"]
pickle.dump(cn,fp)
fp.close()