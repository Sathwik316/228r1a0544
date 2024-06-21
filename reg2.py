'''
import re

text="welcome to cmrec kandhakoya"
b=re.findall("[cmr]{2,5}",text)
print(b)
'''
import re

text="welcome to cmrec kandhakoya"
b=re.sub("[aeiou]","#","text")
print(b)