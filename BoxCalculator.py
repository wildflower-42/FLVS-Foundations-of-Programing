#Alaska Miller
#6/7/2020
#Purpose: This program exists to calculate the volume and surface area of a set of 3 cube boxes with 3 different sets if dimensions, and then informing the end user of the results of their inputs,
#as well as what the results of those inputs SHOULD have been.
#This line imports the python math module
from math import*
#This section of code is where most of the actual calculations and other functions are preformed:
def main():
#This section of the code prints the word problem for the human end user to read:
  print("Question 1:")
  print("")
  print("Thomas is buying boxes to wrap presents in,")
  print("but he wants to know exactly how much space is in each box that he is getting so he knows how many of each to buy,")
  print("there are three sizes of boxes, each is a cube: there is a 3 by 3 by 3 foot box, 6 by 6 by 6 foot  box, and a 12 by 12 by 12 foot box.")
  print("")
  print("What is the volume of each box?")
#This section of code prompts the human end user to enter the information that the program needs to complete the calculations it needs to find the volume of the box.
  box1 = float(input("What is the area of one side of the 3 by 3 by 3 box? "))
  box2 = float(input("What is the area of one side of the 6 by 6 by 6 box? "))
  box3 = float(input("What is the area of one side of the 12 by 12 by 12 box? "))
#This section of code calculates the volume of each size of box based on the input of the human end user.
  boxVol1 = float(pow(box1,3))
  boxVol2 = float(pow(box2,3))
  boxVol3 = float(pow(box3,3))
#This section of code calculates the ACTUAL volume of each box, integers are used because if the math is being done correctly,
#there should not be any float values in the answer, only whole numbers.
  volAns1 = int(pow(3,3))
  volAns2 = int(pow(6,3))
  volAns3 = int(pow(12,3))
#This section of code turns those calculations into strings that can be printed:
  boxVol1 = str(boxVol1)
  boxVol2 = str(boxVol2)
  boxVol3 = str(boxVol3)
#This section prints the volumes of the different sizes of boxes and what the correct answer is.
  print("Your answer for the volume of the 3x3x3 box is: " + str(boxVol1) +" sqft, the correct answer is " + str(volAns1))
  print("")
  print("Your answer for the volume of the 6x6x6 box is: " + str(boxVol2) +" sqft, the correct answer is " + str(volAns2))
  print("")
  print("Your answer for the volume of the 12x12x12 box is: " + str(boxVol3) +" sqft, the correct answer is " + str(volAns3))
  print("")

#This section of code informs the user that the program is finding the surface area of each kind of box now:
  print("Now Thomas needs to find the amount of wrapping paper he needs per box. This program has calculated that too though!")
#This section of the code calculates the surface area of each box and assigns variables to them based upon the user's initial input:
  boxSurf1 = float(pow(box1,6))
  boxSurf2 = float(pow(box2,6))
  boxSurf3 = float(pow(box3,6))
#This section of the code calculates the ACTUAL answer to how much surface area each box has, the program is instructed to use integers because if the math is being done correctly.
#it should always come up with a whole number.
  surfAns1 = int(pow(3,6))
  surfAns2 = int(pow(6,6))
  surfAns3 = int(pow(12,6))
#This section of code prints out the results of the calculations int he previous section of code and informs the human end user of what the correct answer should be based upon a second calculation:
  print("")
  print("Here are the results we generated based on your initial input, and also what the correct answer actually is:")
  print("The surface area of the 3x3x3 box is: " + str(boxSurf1) + " sqft, the actual answer is " + str(surfAns1) + " sqft")
  print("")
  print("The surface area of the 3x3x3 box is: " + str(boxSurf2) + " sqft, the actual answer is " + str(surfAns2) + " sqft")
  print("")
  print("The surface area of the 3x3x3 box is: " + str(boxSurf3) + " sqft, the actual answer is " + str(surfAns3) + " sqft")
main()
