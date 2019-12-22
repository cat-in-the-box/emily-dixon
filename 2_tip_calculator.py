bill = float(input('What is your total bill? '))
tip = float(input('What percent tip will you leave? '))
totalbill=(bill*(1+tip/100))
print("Your total bill is $" ,totalbill,".")
