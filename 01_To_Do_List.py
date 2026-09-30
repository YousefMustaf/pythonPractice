
#  Here's my first to do list app CLI APP, and guess what it's working :)
list = []

while True:
  print("""
  1. Add item
  2. View item
  3. Remove item
  4. Exit
  """)
  command = input("> ")
  if command == '1' or command == 'Add' or command == 'Add item':
    object = input("Write down what you want to add to the list> ")
    list.append(object)

  elif command == '2' or command == 'View' or command == 'View item':
    print(list)

  elif command == '3' or command == 'Remove' or command == 'Remove item':
    object = input("Write down what you want to Remove from the list> ")
    list.remove(object)
    
  elif command == '4' or command == 'Exit':
    break
  else:
    print("Please Enter a Valid Command")