ar1=[2,5,6,8,9]
ar2=[2,5,6]
common_array=[]
for i in ar1:
    if i in ar2:
        common_array.append(i)
print(common_array)