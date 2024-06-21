fp1=open("cse a1.txt","r")
if fp1:
    print("File is opened Successfully")
    fp1.seek(10, 0)
    for i in fp1:
        print(i)
    '''content=fp1.read()
    print(content)
    content=fp1.readline()
    print(content)'''
    fp1.close()