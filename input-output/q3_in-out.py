#Q.3 Write a program named age.py that asks the user to enter their age, then calculates and reports the 
# future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.

age = input("How old are you?\n")

print(f'You are {age} old.')
print(f'In 10 years you will be {int(age) + 10} years old.')
print(f'In 20 years you will be {int(age) + 20} years old.')
print(f'In 30 years you will be {int(age) + 30} years old.')
print(f'In 40 years you will be {int(age) + 40} years old.')