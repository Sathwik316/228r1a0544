def is_eligible_vote(age):
    if (age >= 18):
        return True
    else:
        return False

age = int(input("Enter the age: "))

if is_eligible_vote(age):
    print(age, "is eligible for voting.")
else:
    print(age, "is not eligible for voting.")