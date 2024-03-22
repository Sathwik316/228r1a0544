try:
    a=int(input("Enter the a value"))
    b=int(input("Enter the a value"))
    #c=a/b
    print("value of c:",a+b)
    x=[1,2,3,4]
    print(x[5])
except NameError:
    print("b value is not mentioned")
except ZeroDivisionError:
    print("Arithmatic axception")
except ValueError:
    print("value error")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("key error")
except IOError:
    print("file input or output error")
