import re
file = open("read.txt")

AOC = 0
KC = 0
PaC = 0
PuC = 0
IC = 0
NC = 0

Arithmetic_operators = {'+': 'Addition', '-': 'Subtraction', '/': 'Division','*': 'Multiplication op','=': 'Equal'}
Arithmetic_operators_key = Arithmetic_operators.keys()

#Logical_operators = {'==': 'Equal', '>=': 'Grater equal', '<=': 'Less equal'}
#Logical_operators = Logical_operators.keys()

numbers = {'0':'Constant','1':'Constant','2':'Constant','3':'Constant','4':'Constant','5':'Constant','6':'Constant','7':'Constant','8':'Constant','9':'Constant',}
numbers_key = numbers.keys()

Keyword = {'int': 'integer type', 'float': 'Floating point', 'char': 'Character type', 'long': 'long int'}
Keyword_key = Keyword.keys()

Parenthesis = {'(': 'Rounded brackets', ')': 'Rounded brackets', '{': 'Curly brackets ', '}': 'Curly brackets ', '[': 'Square brackets', ']': 'Square brackets'}
Parenthesis_key = Parenthesis.keys()

punctuation_symbol = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {'a': 'id', 'b': 'id', 'c': 'id', 'd': 'id', 'e': 'id', 'f': 'id', 'g': 'id', 'h': 'id', 'i': 'id', 'j': 'id', 'k': 'id', 'l': 'id',
              'm': 'id', 'n': 'id', 'o': 'id', 'p': 'id', 'q': 'id', 'r': 'id', 's': 'id', 't': 'id', 'u': 'id', 'v': 'id', 'w': 'id', 'x': 'id', 'y': 'id', 'z': 'id'}
identifier_key = identifier.keys()

a = file.read()

count = 0
program = a.split("\n")
for line in program:
    count += 1
    #print("line#", count, "\n", line)

    tokens = line.split(' ')
    print("Tokens are ", tokens)
    #print("Line#", count, "properties \n")
    for token in tokens:
        if token in Arithmetic_operators_key:
            print(token,"is operator ", Arithmetic_operators[token])
            AOC += 1
        if token in Keyword_key:
            print(token,"is datatype ", Keyword[token])
            KC += 1
        if token in punctuation_symbol_key:
            print(token, "symbol is Punctuation ", punctuation_symbol[token])
            PuC += 1
        if token in Parenthesis_key:
            print(token,"is Parenthesis ", Parenthesis[token])
            PaC += 1
        if token in identifier_key:
            print(token, "is Identifier ", identifier[token])
            IC += 1
        if token in numbers_key:
            print(token,"is Constant",numbers[token])
            NC += 1

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")


print("Arithmetic operators (",AOC,")")
print("Keyword ("+ str(KC) +")")
print("Parenthesis ("+str(PaC)+")")
print("Punctuation ("+str(PuC)+")")
print("Identifier (",IC,")")
print("Constant (",NC,")")