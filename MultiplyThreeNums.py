def multiply_three_numbers(a, b, c):
	return a * b * c

if __name__ == "__main__":
	num1 = float(input("First number: "))
	num2 = float(input("Second number: "))
	num3 = float(input("Third number: "))
	res = multiply_three_numbers(num1, num2, num3)
	print(f"The result is: {res}")
