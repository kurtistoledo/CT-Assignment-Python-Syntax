# 7. Exploring Logical Operations and Precedence
# Task 2: Validating Calculations
results = 10 * 2 + 5

parentheses = 10 * (2 + 5)

if results == parentheses:
    print("Both results match:", results)
else:
    print("Results don't match!")
    print("Result without parentheses:", results)
    print("Result with parentheses:", parentheses)

'''
Results don't match!
Result without parentheses: 25
Result with parentheses: 70
'''
