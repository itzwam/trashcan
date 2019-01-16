for i in range(0,100+1):
  result = ""
  result += "Fizz" if i % 3 == 0 else ""
  result += "Buzz" if i % 5 == 0 else ""
  print(result if result else i)
