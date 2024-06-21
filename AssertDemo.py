def avg(marks):
    assert len(marks) != 0,"The list is empty."
    return sum(marks)/len(marks)

marks1 = [67,59,86,75,92]
print("The Average of marks1:",avg(marks1))
marks2 = [10,20,30,40]
print("The Average of marks2:",avg(marks2))