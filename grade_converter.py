# FILE NAME - grade_converter.py

# NAME: Casey Gantz
# DATE: 3/1/26
# BRIEF DESCRIPTION:  converting grades from a number value to a letter value



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def convert_grade(score):
    if score > 100:
        return "A+"
     
    elif score >= 90:
        return "A"
     
    elif score >= 80:
        return "B"
     
    elif score >= 70:
        return "C"
     
    elif score >= 60:
        return "D"
     
    else:
        return "F"
     
try:
    num = float(input("Enter a numerical grade (1-100): "))
    print(convert_grade(num))
except ValueError:
    print("Please enter a valid number.")







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Remember indentations. Frequently code just dosent run when the parts underneath arent indented. 





'''
