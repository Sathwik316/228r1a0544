n=int(input("Enter no of values"))
dic={}
for i in range(n):
    ref=input("Enter kay")
    value=input("Enter value")
    dic[key]=value

    print(dic)
    print("after invertion")
    print(invert_content(dic))

    def invent_content(dic):
        invent_dic={}
        invent_dic={v:k for k,v in dic.items()}
        return invert_dic