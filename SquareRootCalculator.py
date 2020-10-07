# Math Module
#Imports Math Module
from math import *

def main():
#Promts the user to input x and Y variables:
    num = float(input("Input X "))
    exp = float(input("Input Y "))
#Calculates and creates new output variables for the printed anwsers:
    p = pow(num, exp)
    s = sqrt(num)
#Prints the results of the calculations
    print(str(num) + " to the power of " + str(exp) + " is " + str(p) )
    print("The square root of "+str(num)+" is: "+str(s))
main()
