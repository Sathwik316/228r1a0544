'''
import re
text='welcome to cmrec'
k=re.findall("ec$",text)
print(k)
'''
'''
import re
text='welcome to cmrec'
b=re.findall("co+","text");
print(b)
'''
import re

text="ab ab cd ef gh"
b=re.sub("\s","#","text")
print(b)