#reverse order of list
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)

sum_grades=sum(grades)
avg_grades=sum_grades/len(grades)
print(grades)
print(f"The average grade was: {avg_grades} ") 
