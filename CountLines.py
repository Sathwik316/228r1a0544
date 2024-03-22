fp=open("count.txt","r")
words=[]
lines=0
charcount=0
for i in fp:
    charcount++
    words+=i.split( )
    lines+=readline()
print(charcount)
print(lines)