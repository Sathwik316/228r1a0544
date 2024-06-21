import shelve

Sh = shelve.open("shelve")
with shelve.open("shelve") as sh:
    sh['one'] = 1
    sh['two'] = 2
    sh['three'] = 3

sh.close()