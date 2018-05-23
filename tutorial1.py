name = raw_input("What's your name? ")
print "Nice to meet you " + name + " :) "

x = "Hello"
z = "Bye"
print z

def add():
 print 1 + 1
add()

def add():
 return 1 * 4
# print 2* add()

def printThis(word):
  print word
  
printThis("hello")

def printThis(word):
  print word

printThis(421221)

def add(firstNumber, secondNumber):
  return firstNumber + secondNumber
  
print add(10, 20)

def add(firstNumber, secondNumber):
  return firstNumber + secondNumber
  
def subtract(number1, number2):
  return number1 - number2 

def multiply(number3, number4):
  return number3 * number4 

def divide(number5, number6):
  return float(number5) / float(number6)
  
print add(10, 20)
print subtract(30, 10)
print multiply(4, 5)
print divide(5, 2)




def add(firstNumber, secondNumber):
  return firstNumber + secondNumber
  
def subtract(number1, number2):
  return number1 - number2 

def multiply(number3, number4):
  return number3 * number4 

def divide(number5, number6):
  return float(number5) / float(number6)
  
def workout(): 
  choice = input ("Do you want to: 1. Add, 2.Subtract, 3.Multiple, 4.Divide? ")
  
  firstNumber = input("Whats your first number?")
  secondNumber = input("Whats your second number?")
  
  if choice == 1: 
    print " Your answer is: " + str(add(firstNumber, 
      secondNumber))
  elif choice == 2: 
    print " Your answer is: " + str(subtract(firstNumber, 
      secondNumber))
  elif choice == 3: 
    print " Your answer is: " + str(multiply(firstNumber, 
      secondNumber)) 
  elif choice == 4: 
    print " Your answer is: " + str(divide(firstNumber, 
      secondNumber))
  
workout()

word = input("Give me a word")
for letter in word:
  print letter

word = input("Give me a word")
for letter in word:
  print letter + letter


