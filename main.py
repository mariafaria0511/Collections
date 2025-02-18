#Collections_Assignment
studentName = input("Enter the student name:\n")
value1 = int(input("Enter a grade:\n"))
value2 = int(input("Enter a grade:\n"))
value3 = int(input("Enter a grade:\n"))
value4 = int(input("Enter a grade:\n"))
value5 = int(input("Enter a grade:\n"))

valuesList = [value1, value2, value3, value4, value5]
solve = sum(valuesList)/ 5
print(studentName)
print("Average:{}".format(solve))

if solve >= 90:
    print("Letter grade: A")
elif solve >= 80:
    print("Letter grade: B")
elif solve >= 70:
    print("Letter grade: C")
elif solve >= 60:
    print("Letter grade: D")
else:
    print("Letter grade: F")
#
