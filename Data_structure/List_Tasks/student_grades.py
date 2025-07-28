grades = [87,90,76,54,96]
grades.append(88) #adding the grade 
average_grade = sum(grades) / len(grades) # calculate the average grade 
print(f"Average Grades: {average_grade}")
highest_grade = max(grades) # finding the highest and lowest grade 
lowest_grade = min(grades)
print(f"Highest Grade:{highest_grade}")
print(f"Lowest Grade:{lowest_grade}")