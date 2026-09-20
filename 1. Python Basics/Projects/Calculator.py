# Gathering Inputs
first_number = float(input("Enter Your First Number: "))
math_operator = input("Enter Your Operator [+,-,*,/,**,//,%]: ").strip()
second_number = float(input("Enter Your Second Number: "))


if math_operator == "+":
    result = first_number + second_number
elif math_operator == "-":
    result = first_number - second_number
elif math_operator == "*":
    result = first_number * second_number
elif math_operator == "/":
    result = first_number / second_number
elif math_operator == "**":
    result = first_number ** second_number
elif math_operator == "//":
    result = first_number // second_number
elif math_operator == "%":
    result = first_number % second_number
else:
    result = None
result_type = type(result)

calc_history = {
    "first_number" : first_number,
    "operator" : math_operator,
    "second_number" : second_number,
    "result" : result,
    "result_type" : result_type
}

operator_result = calc_history.get("result", result)
type_result = calc_history.get("result_type", result_type)

summary = f"{first_number} {math_operator} {second_number} = {result}\n Your Result is {result_type}"
print(summary)

