#basic_elif.py
# Program to assign grades based on score using if-elif-else
score = int(input("Enter your score (0-100): ")) #to get user input
if 90 <= score <= 100:
    grade = 'A+'
elif 80 <= score < 89:
    grade = 'B'
elif 70 <= score < 79:
    grade = 'C'
elif 60 <= score < 69:
    grade = 'D'
elif 0 <= score < 59:
    grade = 'F'
else:
    grade = 'Invalid score'
print(grade)