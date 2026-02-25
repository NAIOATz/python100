# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

# bmi is equal to the person's weight divided by the person's height squared.
# bmi = weight / (height ** 2)

weight = float(input("Input your weight(kg.): "))
height = float(input("Type your height(m.): "))

bmi = round(weight / (height ** 2))

print(f'This is your BMI : {bmi}')