def remove_duplicate(li):
    unique_list=[]
    duplicate_list=[]

    for i in range(li):
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicate_list.append(i)
            return unique_list
        li=[]
        print(li)
        print(remove_duplicate(li))
