#Alaska Miller
#6/19/2020
#The perpouse of this program is to allow the user to draw a custome image with the cursor using keyboard inputs, that can be stopped and completed when the user uses a command to end the program, based off an "end" command in the "while" loop that generates an image that the user can then view without interuption until the program is restarted or quit:
import turtle
def main():
#This section of code creates variables that can be utilized in the "while" loop a little lower down, that provides for the input loop needed to create lines in the output box:
  menuInput = str("null")
  wasdSprite =turtle.Turtle()
#This section of code creates a series of "if" statements that corespond to menu options in the text promt of the menu promt, these if statements then move the turtle, and therefore this allows the human end user of the program to draw creatively with the program!:
  while (menuInput != str('end')):
    wasdSprite.color("red")
    menuInput = input(""""Please select an option:
    w = Move forward
    s = Move Back
    e = Turn 10 degrees left
    e = Turn 10 degrees left
    a = Turn 90 degrees left
    d = Turn 90 degrees left
    type "end" to exit the program!""")
    if(menuInput == str("w")):
      wasdSprite.forward(100)
    elif(menuInput == str("s")):
      wasdSprite.backward(100)
    elif(menuInput == str("q")):
      wasdSprite.left(10)
    elif(menuInput == str("e")):
      wasdSprite.right(10)
    elif(menuInput == str("a")):
      wasdSprite.left(90)
    elif(menuInput == str("d")):
      wasdSprite.right(90)
    elif(menuInput == str("end")):
      print("end")
    else:
      print("Error: Invalid command!")
main()
