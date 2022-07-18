# image gotten from ascii.co.uk/art
print('''  *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______
*******************************************************************************''')
print('''     .-.
           [.-''-.,
           |  //`~\)
           (<| 0\0|>_
           ";\  _"/ \\_ _,
          __\|'._/_  \ '='-,
         /\ \    || )_///_\>>
        (  '._ T |\ | _/),-'
         '.   '._.-' /'/ |
         | '._   _.'`-.._/
         ,\ / '-' |/
         [_/\-----j
    _.--.__[_.--'_\__
   /         `--'    '---._
  /  '---.  -'. .'  _.--   '.
  \_      '--.___ _;.-o     /
    '.__ ___/______.__8----'
''')
print("Welcome to treasure island adventure game\nYour goal is to find the treasure")
print("You will answer a series of question right that will lead you to the treasure")

choice1 = input("Your found yourself in an unknown plant, with a large book of instructions or guide\nDo you read the first or you go on living and exploring the planet?\nREAD OR EXPLORE\n").lower()
if choice1=="read":
  print("You made the right choice; The book is the Bible we are given to pass through this planet Earth")
  choice2 = input("After reading the book, will you obey the rules and instructions given, though they may seem impossibe OBEY or IGNORE\n").lower()
  if choice2 == "obey":
    print("Proceed to the Next Stage; Obeying the instructions will guide you no matter how vague it may seem")
    choice3 = input("You have arrived at the final stage\nThe question is are you willing to \"DIE\", \"PAY THE PRICE\", \"DENY YOURSELF FOR THE TRESSURE\"\nYES OR NO\n").lower()
    if choice3 == "yes":
      print("The door of Tresures are open unto; Go in and Enjoy")
    else:
      print("Game over, you need to give yourself for the treasure")
  else:
    print("Game Over; couldn't find the treasure!!! Try Again")

else:
  print("Game over; You won't live forever after you have found the treasure")