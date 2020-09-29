#Alaska Miller
#6/23/2020
#The Perpouse of this program is to promt the human end user anwser a series of questions and then check the anwnsers of those questions against a previously recorded list of responses and checks the inputed responses against those, if they match then the user is told they may join a club, if not they are denied membership:
def main():
  #This section of code creates a blank list and a predermined "answer" list:
  inputList = []
  ansList = ["N/A","y","y"]
  #This section of code promts the human end user to either begin the process for applying to join the club, or thanks them for their time if they do not want to join the club:
  promtYn = input("Do you want to join a coding club? (y/n):")
  if promtYn == "y":
    #This section of code asks the human end user if they are okay with answering some questions about themselves in order to join, and then either runs a set of code to get that input they need to create
    areYouSure = input("Great, but first we need to ask you some questions, is this okay with you? (y/n):")
    if promtYn == "y":
      #This section of code promts the human end user to answer three questions, and then records the responses of all three, even though the first question is not actually applicable as to whether or not you will actually get into club, and exists soley for stastical perpouses:
      questionOne = input("Okay good! So our first question is, do you know any sort of programing langauge (y/n):")
      if questionOne == "y":
        print("Okay good! So our first question is, do you know any sort of programing langauge (y/n): "+str(questionOne))
        inputList.append("y")
      if questionOne == "n":
        print(" ")
        print("Okay good! So our first question is, do you know any sort of programing langauge (y/n): "+str(questionOne))
        inputList.append("n")
      questionTwo = input("Now for question 2, are you willing to contribute to a safe and postive enviroment for our club? (y/n): ")
      if questionTwo == "y":
        print(" ")
        print("Now for question 2, are you willing to contribute to a safe and postive enviroment for our club? (y/n): "+str(questionTwo))
        inputList.append("y")
      if questionTwo == "n":
        print(" ")
        print("Now for question 2, are you willing to contribute to a safe and postive enviroment for our club? (y/n): "+str(questionTwo))
        inputList.append("n")
      questionThree = input("Okay third and final question, are you willing to learn new things over the course of being in this club? (y/n): ")
      if questionThree == "y":
        print(" ")
        print("Okay third and final question, are you willing to learn new things over the course of being in this club? (y/n): "+str(questionThree))
        inputList.append("y")
      if questionThree == "n":
        print(" ")
        print("Okay third and final question, are you willing to learn new things over the course of being in this club? (y/n): "+str(questionThree))
        inputList.append("n")
      #This section of code checks if the user inputed question responses to both question #2 or #3 match the required awnsers in the "ansList" list, and if so, welcomes the user to the club, if not they politely reject them from membership:
      if inputList[1] == ansList[1] and inputList[2] == ansList[2]:
        print(" ")
        print("Congradulations! You can join the coding club!!!")
        if inputList[0] == str("y"):
          print(" ")
          print("We are glad to have someone who is allready exprienced in the club!")
        print(" ")
        print("We are also glad that you are willing to work with others and learn from others as well!")
      if inputList[1] != ansList[1] and inputList[2] != ansList[2]:
        print("We are sorry but we don't think you are the kind of person we are looking for in our club, we are truely sorry, please contact the club administrator if you belive this to be a mistake!")
    if promtYn == "n":
      print("Sorry but these questions are required to gain club membership")
  if promtYn == "n":
    print("Okay thank you for your time")
main()
