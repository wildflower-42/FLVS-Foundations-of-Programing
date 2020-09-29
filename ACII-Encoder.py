#Alaska Miller
#6/25/2020
#The purpouse of this program is to translate a user-inputed message into ASCII code and then back again into plaintext:
def main():
  #This line of code defines the lists needed for the program later on:
  messageLetList = []
  messageDecodeList = []
  #This section of code takes the yser's input and stores it in both a list and creates a variable to 
  userInput = input("Please enter a message: ")
  inputList = list(userInput)
  inputLength = len(inputList)
  #This section of code creates a loop that takes the list made in the previous section of code and uses the ".appened" command to endcode the letters of the user's input into ASCII code and then stores it in the: "messageLetList[]" list, and then prints that list neatly:
  for n in range(inputLength): 
    messageLetList.append(ord(inputList[n]))
  print("This is your encoded message: ")
  print(messageLetList[0:])
  #This section of code decodes the encoded message:
  LetListLength = len(messageLetList)
  #This section of code creates a loop that decodes the values of "messageLetList" and then puts them in the: "messageDecodeList[]" list using the uses the ".appened" command, then prints that list:
  for n in range(LetListLength): 
    messageDecodeList.append(chr(messageLetList[n]))
  print("This is your plaintext decoded message: ")
  print("".join(messageDecodeList))
main()
