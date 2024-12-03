print("Welcome to the Average Height Calculator!")
# Convert input str into list
height = input("Enter height separated by space: \n").split(" ")
# Convert input str to int
for i in range(0, len(height)):
    height[i] = int(height[i])

# Total up height
total_height = 0
for i in height:
    total_height += i

# Total up number of students
total_student = 0
for i in height:
    total_student += 1

# Calculate avg
avg_height = total_height / total_student
print(avg_height)

