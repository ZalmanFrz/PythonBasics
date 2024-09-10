num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))

operators = input("Choose an Opeator (+, -, *, /, %, **2, **3)")

if operators == "+":
 print(num1 + num2)
elif operators == "-":
 print(num1 - num2 )
elif operators == "*":
 print(num1 * num2)
elif operators == "/":
 print(num1 / num2)
elif operators == "%":
 print(num1%num2 )
elif operators == "**2":
 print(num1 **2 or num2 **2)
else:
 print("wrong input")