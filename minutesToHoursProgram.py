#Alaska Miller
#7/1/2020
#The perpouse of this program is to calculate minutes to hours:
#This function converts inputed hours to minutes:
def convertHtoM(hours):
  minutes = int(hours * 60) #This line of code takes the value "hours" and then multiplies it by 60  to give us an output of "minutes", and this makes it so for every one hour there is 60 minutes in the "minutes" output value, therefore creating a conversion for a ratio of 1:60.
  return minutes #This line of code returns the output of the previous line so that the function can be used to caluate a value that is inputed in the "main():" function.
#This function converts inputed minutes to hours:
def convertMtoH(minutes):
  hours = float(minutes / 60) #This line of code takes the value "minutes" and then divides it by 60 to give us an output of "hours", or for every 60 minutes we get one output of "hours", or a ratio of 60:1, therefore creating a conversion for the minutes to hours at a ratio of 1:60.
  return hours #This function returns the output of the previous line so that the function can be used to caluclate a value that is inputed in the "main():" function.
#This function runs the main program for this function which promts the human end user to select from a series of options and then provides them for an input box connected to the apropraite function for each as is apropraite for that menu option:
def main():
  #This section of code creates a variable and input box to assign an input to that variable so that later it can be used as the basis for functions triggered by the "if" statements:
  hOrM = int(input("""Please Select an option to convert:
  1: Minutes to Hours
  2: Hours to Minutes 
  """))
  #This section of code promts the human end user to enter a number of hours, and then outputs a number of minutes based on a function preformed in this section and prints that output in ther terminal:
  if hOrM == 1:
    hoursInput = float(input("""Hours to Minutes Converter: 
    Please enter hours: """))
    print(str(convertHtoM(hoursInput))+str(" minutes"))
  #This section of code promts the human end user, similarly to the previous section of code, but in this case that function converts the inputed number of minutes into hours and outputs that in the terminal:
  elif hOrM == 2:
    minutesInput = float(input("""Minutes to hours Converter: 
    Please enter minutes: """))
    print(str(convertMtoH(minutesInput))+str(" hours"))
  #This section of code prints an errorcode if the user doesn't input a valid menu selection:
  else:
    print("Error101: Invalid Menu Input: Please select a valid menu value")
main()
