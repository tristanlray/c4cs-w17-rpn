#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
}

def functioncall(arg):
	print("This is a function call")

def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)

			stack.append(result)
	return stack.pop()


def main():
	while True:
		result = calculate(raw_input('rpn calc> '))
		if result > 0:
			print colored("Result: ", "blue")
			print colored(result, "green")
		else:
			print colored('Result: ', 'blue')
			print colored(result, 'red')
		

if __name__ == '__main__':
	main()
