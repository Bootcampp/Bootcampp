hwWeight = 0.4
examWeight = 0.5
discussionWeight = 0.1

hwGrade = float(input("Enter your homework grade: "))

examGrade = float(input("Enter your exam grade: "))

discussionGrade = float(input("Enter your discussion grade: "))

totalGrade = (hwWeight * hwGrade) + (examWeight * examGrade) + (discussionWeight * discussionGrade)


print("Your total grade in the class is:", totalGrade)

## a fruitful function are functions that return a value but void functions do not return any value

P = 10000  # Principal amount
n = 12     # Number of times interest is compounded per year
r = 0.08   # Interest rate (8%)

t = int(input("Enter the number of years: "))

amount = P * (1 + (r / n))**(n * t)

print("The final amount after", t, "years is:", amount)




def calculateGPA(score):
    if score >= 80:
        return 4.0
    elif score >= 79:
        return 3.5
    elif score >= 70:
        return 3.0
    elif score >= 65:
        return 2.50
    elif score >= 60:
        return 2.0
    elif score >= 55:
        return 1.5
    elif score >= 50:
        return 1.0
    elif score >= 45:
        return 1.7
    elif score >= 40:
        return 1.0
    else:
        return 0.0

def getHonours(gpa):
    if 3.85 <= gpa <= 4.0:
        return "Honours: Summa Cum Laude"
    elif 3.70 <= gpa <= 3.84:
        return "Honours: Magna Cum Laude"
    elif 3.50 <= gpa <= 3.69:
        return "Honours: Cum Laude"
    else:
        return "No Honours"
    
score = float(input("Enter your numerical score (out of 100): "))
gpa = calculateGPA(score)
print("GPA:", gpa)
honours = getHonours(gpa)
print(honours)





import math

# Input the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = math.pi * radius**2

# Print the result
print("r =", radius)
print("Area =", area)




def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

can_form_triangle = is_triangle(side1, side2, side3)

if can_form_triangle:
    print("It is possible to form a triangle with the given side lengths.")
else:
    print("It is not possible to form a triangle with the given side lengths.")



def check_triangle():
    side1 = int(input("Enter the length of the first stick: "))
    side2 = int(input("Enter the length of the second stick: "))
    side3 = int(input("Enter the length of the third stick: "))

    can_form_triangle = is_triangle(side1, side2, side3)

    if can_form_triangle:
        print("Yes, sticks with the given lengths can form a triangle.")
    else:
        print("No, sticks with the given lengths cannot form a triangle.")

def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

check_triangle()

