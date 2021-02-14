print('Welcome to my "Fantasy Travels" story game')
stop_script = input("Press enter to continue...")
gender =  input("Specify your gender please\n")
#switch() checking gender to call pronouns accordingly
print("so tell me, \nWhat profession would you most prefer to uphold in your dreams?")
character_class = input("Knight\nAssassin\nWizard\n")
#switch (character_class === true) case wizard...
if character_class == "Knight" or character_class == "knight":
  print("Good morning soldiers! Time to line up.")# morning training falls to ruins
if character_class == "Assassin" or character_class == "assassin":
  print("Rise sinner, the shadows follow")# no longer alone in your cave
if character_class == "Wizard" or character_class == "wizard":
  print("Awaken mage, start walking")# being mugged by bandits
