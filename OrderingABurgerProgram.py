#Alaska Miller
#6/8/2020
#Purpouse: To caculate the total of a given meal at a local restruant called "Sharky's Beach Burgers", including tip, tax, and the total cost of the meal:
#NOTICE: PLEASE NOTE THAT THIS PROGRAM'S MENU IS REFLECTIVE OF AN ACTUAL RESTRUANT!
#This section of code imports the math module and sets up the space for the rest of the program to run.
from math import*
def main():
#This section of the code creates and stores values that reflect the prices of menu items at the restruant:
#This subsection of the code creates variables and assigns prices for the burgers with normal toppings and no cheese,
#this is the basis of the burger prices before extra toppings and cheese are added, then creates a list of these prices.
  singleBeef = float(6.00)
  #print(type(singleBeef))
  doubleBeef = float(8.00)
  juicyLucy = float(8.50)
#This subsection of code creates and stores the vaules of code that are associated with the speciality sandwhiches that the restruant serves,
#such as their Vegan burger and sandwhiches that use meats other than beef such as chicken or beef:
  singleChicken = float(7.00)
  singleFish = float(7.00)
  singleVegan = float(8.00)
#This subection of code creates a list of all the entrees on the menu:
  menuEntrees = []
  menuEntrees.append(singleBeef)
  menuEntrees.append(doubleBeef)
  menuEntrees.append(juicyLucy)
  menuEntrees.append(singleChicken)
  menuEntrees.append(singleFish)
  menuEntrees.append(singleVegan)
  #print(menuEntrees)
#This section of code creates variables for additonal toppings that can be added to each of the base entrees, 
#their costs are saved as a sepreate set of variables to that of the entrees, it also creates an "Extras Menu" list,
#Which exists as a shorcut to view and refrence the prices of any extras or toppings one can get on a menu item
  noToppings = float(0.00)
  extrasMenu = [noToppings]
  addCheese = float(1.00)
  extrasMenu.append(addCheese)
  addToppings = float(0.50)
  extrasMenu.append(addToppings)
  addToppingsPlus = float(1.00)
  extrasMenu.append(addToppingsPlus)
#This section of the code creates set of variables for the drinks on the menu:
  smallShake = float(5.00)
  largeShake = float(6.00)
  sodaSmall = float(2.59)
  sodaLarge = float(2.99)
  teaSmall = float(2.59)
  teaLarge = float(2.99)
#This subsection creates a list of all drinks on the menu:
  menuDrinks = []
  menuDrinks.append(smallShake)
  menuDrinks.append(largeShake)
  menuDrinks.append(sodaSmall)
  menuDrinks.append(sodaLarge)
  menuDrinks.append(teaSmall)
  menuDrinks.append(teaLarge)
  #print(menuDrinks)
  #print(menuDrinks[0])
#This subsection of the code creates a set of variables for additonal charges that can be added to the drinks on the menu, very similar to how toppings are added onto the price of entrees for the main menu:
  addMalt = float(0.50)
  extrasMenu.append(addMalt)
#This section of code creates a set of variables to represent the costs of all the sides on the menu, and then creates a list of them:
  smallFries = float(3.00)
  largeFries = float(3.50)
  cheeseFries = float(4.00)
  onionRings = float(5.00)
  cajunTots = float(3.50)
  unicornTots = float(3.50)
#This subsection of code compiles all the menu items that are sides into a list at their base price:
  menuSides = []
  menuSides.append(smallFries)
  menuSides.append(largeFries)
  menuSides.append(cheeseFries)
  menuSides.append(onionRings)
  menuSides.append(cajunTots)
  menuSides.append(unicornTots)
  #print(menuSides)
#This subection creates a variable that can be added to one of the side menu items:
  addBacon = float(1.00)
  extrasMenu.append(addBacon)
  #print(extrasMenu)
#This part of the code creates variables for each part of the order:
  entreeCost = 0.00
  drinkCost = 0.00
  sideCost = 0.00
#This section of the code creates variables for the promts that will presented as part of "if" statements, these variables are designed to be overwritten:
  maltedYn = str("null")  
  baconYn = str("null")
  sideName = str("null")
  entreeName = str("null")
  drinkName = str("null")
#This section of code prompts the user to enter what they want to buy from the restruant and gives them a list of things they could buy:
  userEntree = input("""Please select an entree menu item and type in it's number: 
  1. $6.00: Single Patty 
  2. $8.00: Double Patty
  3. $8.50: Juicy Lucy "Loaded" patty (filled with provolone cheese)
  4. $7.00: Chicken Sandwhich
  5. $7.00: Fish Sandwich
  6. $8.00: Beyond Burger (Burger with meat subsitute)
  """)
#This section of code lists "if" statements that refrence the "menuEntrees" list created earlier in the program in order to find prices for each menu item:
  if(userEntree == "1"):
      entreeCost = menuEntrees[0]
      entreeName = str("Beef Burger")
  if(userEntree == "2"):
      entreeCost = menuEntrees[1]
      entreeName = str("Double Beef Burger")
  if(userEntree == "3"):
      entreeCost = menuEntrees[2]
      entreeName = str("Juicy Lucy Burger")
  if(userEntree == "4"):
      entreeCost = menuEntrees[3]
      entreeName = str("Chicken Sandwich")
  if(userEntree == "5"):
      entreeCost = menuEntrees[4]
      entreeName = str("Fish Sandwich")
  if(userEntree == "6"):
      entreeCost = menuEntrees[5]
      entreeName = str("Vegan Burger")
#This section of code asks the end user for input about what toppings they want on their entree and then uses "if" statments do decide how much they need to add on to the inital cost of the entree:
  userToppings = input("""Please select a topping option and type in it's number: 
  0. $0.00: None (Select if you don't want any toppings)
  1. $1.00: Add cheese
  2. $0.50: Add a regular topping (carmelized onions, pinapple, jalapenos, or potato sticks)
  3. $1.00: Add a premium topping (bacon, egg, portabella mushroom, fried green tomato, an onion ring, or queso
  """)
  if(userToppings == "0"):
    entreeCost = entreeCost + extrasMenu[0]
  if(userToppings == "1"):
    entreeCost = entreeCost + extrasMenu[1]
  if(userToppings == "2"):
    entreeCost = entreeCost + extrasMenu[2]
  if(userToppings == "3"):
    entreeCost = entreeCost + extrasMenu[3]
  #print(entreeCost)
#This section prompts the user to select a drink from a menu, if they select a shake though, they will be promted to decide what they want on that shake:
  userDrink = input("""Please select a drink option and type in it's number:
  0. $0.00: No Drink
  1. $5.00: Small Shake
  2. $6.00: Large Shake
  3. $2.59: Small Fountain Drink
  4. $2.99: Large Foundtain Drink
  5. $2.59: Small Iced Tea
  6. $2.99: Large Iced Tea
  """)
  if(userDrink == "O"):
    drinkCost = 0
#This section of code creates a second prompt if you select a shake:
  if(userDrink == "1"):  
    maltedYn = input("Do you want your shake malted for $0.50? (y or n)")
    if(maltedYn == "y"):
      #print(menuDrinks[0])
      drinkCost = menuDrinks[0] + extrasMenu[4]
      drinkName = str("Small Malted Milkshake")
    if(maltedYn == "n"):
      drinkCost = menuDrinks[0]
      drinkName = str("Small Milkshake")
  if(userDrink == "2"):
    maltedYn = input("Do you want your shake malted for $0.50? (y or n)")
    if(maltedYn == "y"):
      drinkcost = float(menuDrinks[1]) + float(extrasMenu[4])
      drinkName = str("Large Malted Milkshake")
    if(maltedYn == "n"):
      drinkcost = float(menuDrinks[1])
      drinkName = str("Large Milkshake")
  if(userDrink == "3"):
    drinkCost = menuDrinks[2]
    drinkName = str("Small Fountain Drink")
  if(userDrink == "4"):
    drinkCost = menuDrinks[3]
    drinkName = str("Large Fountain Drink")
  if(userDrink == "5"):
    drinkCost = menuDrinks[4]
    drinkName = str("Small Iced Tea")
  if(userDrink == "6"):
    drinkCost = menuDrinks[5]
    drinkName = str("Large Iced Tea")
#This section of code creates a prompt for the user to select a side for their meal:
  userSide = input("""Please select a side and type in it's number: 
  0. $0.00: No Side
  1. $3.00: Small Hand cut Fries
  2. $3.50: Large Hand cut Fries
  3. $4.00: Queso Fries
  4. $5.00: Onion Rings
  5. $3.50: Cajun Sweet Potato Tots
  6. $3.50: Unicorn Sweet Potato Tots (Sweet Potato Tots but covered in rainbow sprinkles and marshmellows!
  """)
#This section of code tells the program what side they got and how much it costs:
  if(userSide == "0"):
    sideCost = 0
  if(userSide == "1"):
    sideCost = menuSides[0]
    sideName = str("Small fries")
  if(userSide == "2"):
    sideCost = menuSides[1]
    sideName = str("Large Fries")
#This section of code promts the user to decide if they want to get bacon on their queso fries for $1.00)
  if(userSide == "3"):
    baconYn = input("Do you want to add bacon on that for $1.00? (y or n)")
    if(baconYn == "y"):
      sideCost = menuSides[2] + extrasMenu[5]
      sideName = str("Queso fries with bacon")
    if(baconYn == "n"):
      sideCost = menuSides[2]
      sideName = str("Queso fries")
  if(userSide == "4"):
    sideCost = menuSides[3]
    sideName = str("Onion Rings")
  if(userSide == "5"):
    sideCost = menuSides[4]
    sideName = str("Cajun Sweet Potato Tots")
  if(userSide == "6"):
    sideCost = menuSides[5]
    sideName = str("Unicorn tots")
  #print(sideCost)
#This section of code caclulates the entire cost of the meal and then turns the costs of each component into a string to be printed out:
  totalCost = (entreeCost + drinkCost + sideCost)
  #print(totalCost)
  entreeCost = str(entreeCost)
  drinkCost = str(drinkCost)
  sideCost = str(sideCost)
  withTip = round(float(totalCost * 0.020),2)
  withTaxes = round(float(totalCost * 1.065),2)
  fullCost = round(float(withTaxes + withTip),2)
#This section of code changes the totalCost, withTip, withTaxes, and fullCost variables into printable strings:
  withTip = str(withTip)
  withTaxes = str(withTaxes)
  fullCost = str(fullCost)
  totalCost = str(totalCost)
#This section of code prints a list of what was ordered, and how much it cost:
  print("Order Receipt:")
  print("")
  print(entreeName + ": $"+entreeCost)
  print(drinkName + ": $"+drinkCost)
  print(sideName + ": $"+sideCost)
  print("")
  print("Total cost before taxes: $" + totalCost)
  print("Total cost after taxes: $" + withTaxes)
  print("The expected gratuity (20%) owed: $" + withTip)
  print("Total expected price of meal: $" + fullCost)
main()
