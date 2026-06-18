print('------ PYTHON ORACLE OF WISDOM ------')

print("Hello! What questions about Python do you have today?")


running_oracle = True

while running_oracle:

  command = input('Please type only the topic of your question. To quit, type exit: ').lower().strip()

  match command:

    case 'variables' | 'variable':
      print("Variable or variables, are like labeled boxes in the memory of the computer where we store data. To create in Python, you don't have to say the type (like text or number); Python discovers it by itself!! Exemple: age = 25 -> it creates a labeled box called 'age' with number 25 inside.")

    case 'type of data' | 'types':
      print("Python has four main types of primitive data: str (texts between quotation marks), int (integer numbers), float (numbers with decimal point, like 1.75) and bool (True or False). Knowing the types prevents you from trying to add a word with a number for mistake!")

    case 'list' | 'lists':
      print("List or lists allows that you store multiple values in one variable, sorted by a order (indice) that always starts with zero. They stays between brackets, example: fruits = ['apple', 'banana', 'grape']. You can add itens with .append() and remove with .remove().")   

    case 'conditionals' | 'if' | 'else' | 'if else' | 'elif':
      print("The conditionals are used to made the program take decisions based in rules of 'If' and 'Elif'. We use 'if' for the first condition, 'elif' in the case of try another especific options in halfway, and 'else' for the rest, if none of previous options is true.")

    case 'loop' | 'repetition' | 'repetition structures':
      print("Loops are used to repeat one code block without you needing to rewrite it several times. We use 'for' when we know exactly how many times we wanna know repeat (how to navigate a list of names) and we use the 'while' when the repetition depends of a condition to continue being true.")

    case 'function' | 'functions':
      print("Functions are code blocks reusable that perform a specific task. You create them when you use the keyword 'def'. They could use to receive informations (parameters) and return a result using the 'return'. They avoid the famous 'Ctrl+C e Ctrl+V' in your code.")

    case 'dictionary' | 'dictionaries':
      print("Unlike lists, dictionaries don't use numbers (indices) to find the items, but rather a 'Key' and 'Value' system inside of brackets {}. Example: data = {'name': 'Priscila', 'age': 25}. To find the age, simply search using the keyword: data['age'].") 

    case 'errors' | 'try except':
      print("Mistakes happen! In Python, to prevent your program from 'crashing' and shutting down on the user when something goes wrong. When something goes wrong, we use 'try' and 'except' blocks to handle the error safely")

    case 'exit':
      running_oracle = False
      print("Thank you! See you soon!")   

    case _:
      print("This topic will be added to our assistant soon!")
    
    