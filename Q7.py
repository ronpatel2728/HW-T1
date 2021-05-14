# Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE

import stringcase

if __name__ == '__main__':
   user_input =input("Enter varible value : ")
   print("using Upper CamelCase",stringcase.capitalcase(user_input))
   print("using Lower CamelCase",stringcase.lowercase(user_input))
   print("using UpperCase",stringcase.uppercase(user_input))
