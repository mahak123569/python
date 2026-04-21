marks = int(input("Enter student marks : "))
if(marks >=90):
    gread = "A"
elif(marks >=80 & marks <90):
    grade = "B"
elif(marks >=70 & marks <80):
    grade = "C"   
else:     
   grade ="D"
print("grade of the student ->", grade)   