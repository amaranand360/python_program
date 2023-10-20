class formulaerror(Exception):
  pass

def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  raise formulaerror('{} is not a valid operator'.format(op))


try:
  exp = input("enter your formula!")
  if(len(exp)!=3):
    raise formulaerror("formula is not valid")
  op = exp[1]
  li = exp.split(op) 
  li[0] = float()
  li[1] = float()
  res = calculate(li[0],op,li[1])

except formulaerror as f:
  print(f)

except ValueError as v:
  print(v) 

else:
  print("result ",res)































# class FormulaError(Exception):
#     pass

# def parse_input(user_input):

#   input_list = user_input.split()
#   if len(input_list) != 3:
#     raise FormulaError('Input does not consist of three elements')
#   n1, op, n2 = input_list
#   try:
#     n1 = float(n1)
#     n2 = float(n2)
#   except ValueError:
#     raise FormulaError('The first and third input value must be numbers')
#   return n1, op, n2


# def calculate(n1, op, n2):

#   if op == '+':
#     return n1 + n2
#   if op == '-':
#     return n1 - n2
#   if op == '*':
#     return n1 * n2
#   if op == '/':
#     return n1 / n2
#   raise FormulaError('{op} is not a valid operator'.format(op))


# while True:
#     user_input = input("(Enter 'exit' for exit) Enter the formula: ")
#     if user_input == 'exit':
#         break
#     n1, op, n2 = parse_input(user_input)
#     result = calculate(n1, op, n2)

# print(result)