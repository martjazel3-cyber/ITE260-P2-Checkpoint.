def calculate(a, b, c):
    return (a + b + c) / 3

students = int(input("Number of students: "))

if students < 3:
	print("Required at least 3 students.")
else:
	for i in range(1, students + 1):
         print("Student", i)

         name = input("Student name: ")
         activity1 = int(input("Activity 1: "))
         activity2 = int(input("Activity 2: "))
         activity3 = int(input("Activity 3: "))
  
         average = calculate(activity1, activity2, activity3)

         print("Average:", average)

         if average >= 90:
              print("Status: Very good")
         elif average >= 85:
             print("Status: Good")
         elif average >= 75:
             print("Status: Passed")
         else:
             print("Satatus: Failed")
