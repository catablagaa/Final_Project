# from colorama import Fore
#
# print(Fore.CYAN + 'This text is red in color')



try:
  print(x)
except NameError as e:
  print(f"Variable x is not defined, {e}")
except:
  print("Something went wrong")