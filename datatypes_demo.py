# Here it will give datatype of use variable
a=eval(input("Enter any digit :"))
print(type(a))


#Here permorming arthimatic task on numeric values
a1=int(input("Enter number 1 :"))
a2=int(input("Enter number 2 :"))
sign=input("Choose any one sign and enter [*,-,+,%,//] ")
if sign=="*":
    print(f"Product of {a1} and {a2} is {a1*a2}")
elif sign=="+":
    print(f"Sum of {a1} and {a2} is {a1+a2}")
elif sign=="-":
    print(f"Subtract of {a1} and {a2} is {a1-a2}")
elif sign=="%":
    print(f"Mode of {a1} and {a2} is {a1%a2}")
elif sign=="//":
    print(f"Division of {a1} and {a2} is {a1//a2}")
else:
    print("Invalid Input")


#Conversion sting to integer(Whole numbers) and float(decimal)
ch = input("Enter something: ")
num=int(ch)
print(num)
print(type(num))

ff = input("Enter something: ")
num=float(ff)
print(num)
print(type(num))







