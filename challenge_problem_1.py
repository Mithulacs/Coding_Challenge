# CHALLENGE PROBLEM 1
# SHOULD WE ROUND UP THE FINAL GRADE?

# Every subject is graded from 0 to 100%. Less than 40% is failing grade and more than 80% is a distinction. 
# We can round up a grade:
# If the difference between the  grade and the next multiple of 5  is less than 3, round  up to the next multiple of 5.
# If the value of  is less than 40, no rounding occurs as the result will still be a failing grade.
# Given a input grade, round it up if appropriate and tell us if the student passed, failed or received a distinction.  Write a algorithm and produce a flow chart.

grade = int(input("Enter your grade: "))
if grade >= 40:
    next_m5 = ((grade // 5) + 1) * 5
    if next_m5 - grade < 3:
        next_m5 = grade
if grade >= 0 and grade < 40:
    print("Fail")
elif grade >= 40 and grade < 80:
    print("Pass")
elif grade >= 80 and grade <= 100:
    print("Distinction")
else:
    print("Invalid grade")
  

# def StringChallenge(strParam):

#   # code goes here
#   str = strParam
#   strParam = str.title()
#   return strParam

# # keep this function call here 
# print StringChallenge(raw_input())