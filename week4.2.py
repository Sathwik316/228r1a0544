def remove_duplicate(li):
    unique=[]
    duplicates=[]
    for i in li:
        if i not in unique:
            unique.append(i)
        else:
            duplicates.append()
            return unique

        li=[1,3,4,1,4,5,6,8,5,7]
        print(remove_duplicate(li))