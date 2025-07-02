students_grades={"mark" : [85,90,75],"leo" : [92,88,95],"peter" : [70,75,80]}
for name, grades in students_grades.items():
    average=sum(grades)/len(grades)
print(f"{name} - average grade : {average:.2f}")