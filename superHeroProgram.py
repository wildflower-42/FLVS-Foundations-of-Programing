#Alaska Miller
#7/7/2020
#The perpouse of this program is to create a program that lets the human end user customize a fictitious super hero and then have a short story played back to them in the terminal after they finish customizing their super hero:
#This section of code initizalies the "Hero" class:
class Hero:
  def __init__(self, heroName = "", realName = "",strengthPnts = int(0), speedPnts = int(0),intelPnts = int(0),totalPnts = int(0)):
    self.heroName = heroName
    self.realName = realName
    self.strengthPnts = strengthPnts
    self.speedPnts = speedPnts
    self.intelPnts = intelPnts
    self.totalPnts = totalPnts
  #This method detimrines the total points your character has:
  def totalPoints(self):
    self.totalPnts = int(self.strengthPnts) + int(self.speedPnts) + int(self.intelPnts)

def main():
  #This section of code creates a list of questions that can be called in a "for n range(x):" loop so the human end user can be prompted more easily and the questions don't have to be smushed all into one line:
  heroQuestionsList = [] #This creates the list that will contain all the questions.
  #This section of code degines the questions and adds them to the list from the pervious line:
  heroQuestionsList.append("Please enter your hero's superhero name: ")
  heroQuestionsList.append("Please enter your hero's real name/secret idenity: ")
  heroQuestionsList.append("Please enter your hero's Strength points out of 10: ")
  heroQuestionsList.append("Please enter your hero's speed points out of 10: ")
  heroQuestionsList.append("Please enter your hero's intelegence points out of 10: ")
  #This section of code creates a list that contains the attributes that we will input into our hero class:
  heroAttributesList = [] #This line creates the attributes list we will use to define the attributes of our class.
  #This loop takes the questions from the pervious section of code and gets user feedback from each one, then uses that user feedback input in order to create a list that then is used to create
  for n in range(5):
    listVar = input(heroQuestionsList[n])
    heroAttributesList.append(listVar)
  #This section of code prints the atributes of your hero in the terminal in the form of a story:
  superHero1 = Hero(heroAttributesList[0],heroAttributesList[1],heroAttributesList[2],heroAttributesList[3],heroAttributesList[4])
  print("Your superhero's name is "+str(superHero1.heroName)+",")
  print("but when they are not wearing a cape, they go by: "+str(superHero1.realName)+", but don't tell anyone, it's a secert!!!")
  print(str(superHero1.heroName)+" fights crime hand to hand with their "+ str(superHero1.strengthPnts)+ " points of strength,")
  print("but if things get hairy they can escape with their "+str(superHero1.speedPnts)+" points of speed!!!!")
  print("And last, but certianly not least, they can outsmart the bad guys with their "+str(superHero1.intelPnts)+" intellegence points!")
  superHero1.totalPoints()
  print("Overall they have a grand total of: "+str(superHero1.totalPnts)+" power points out of a possible 30!!!!!")
main()
