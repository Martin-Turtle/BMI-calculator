# This is a sample Python script.
print('BMI CALCULATOR')
print('Please enter your weight and height')
weight = int(input())
height = float(input())
BMI = weight / height ** 2

if BMI <18.5:
    print('Underweight')
elif BMI >=18.5 and BMI <25:
    print("Normal")
elif BMI >=25 and BMI <30:
    print("Overweight")
else :
    print("Obesity")