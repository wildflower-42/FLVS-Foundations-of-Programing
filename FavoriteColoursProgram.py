#Alaska Miller
#6/23/2020
#The Perpouse of this program is to prompt the human end user to input a series of questions that will have them rank their favorite colours, then the program will match them against MY previously listed into the program, favorite colours!
def favoritesCompare():
 #This section of code creates the nessecary variables and lists to preform the functions of the program:
  myFavoriteColours = ["blue","pink","red","black","white"] #This is the List of my favorite colours
  numOfColours = len(myFavoriteColours) #This variable tells us how many colours are in the previous list "myFavoriteColours"
  yourFavoriteColours = [] #This list is blank and is used to be a blank target for the "xyz.appened", so we can pogressively create a list and check it against the "myFavoriteColours" list
  #This section of code is a loop that prompts the human end user to input their favorite colours into a series of promts, ranking them:
  for n in range(0,numOfColours):
    humanListNum = int(n)+int(1)
    inputColours = input(str("please enter your #")+str(humanListNum)+str(" favorite colour:"))
    yourFavoriteColours.append(inputColours)
  #This section of code is a loop that checks the user input against the existing list "myFavoriteColours", and then uses an "if-else" statement to detirmine what it's response should be, then lists the responses:
  for n in range(0,numOfColours):
    if myFavoriteColours[n] == yourFavoriteColours[n]:
      print("Your #"+str(n+1)+" favorite colour is: "+str(yourFavoriteColours[n])+", Mine is too!")
    else:
      print("Your #"+str(n+1)+" favorite colour is: "+str(yourFavoriteColours[n])+", but mine is: "+str(myFavoriteColours[n]))
favoritesCompare()
