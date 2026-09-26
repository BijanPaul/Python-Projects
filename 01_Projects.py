import pyttsx3
engine = pyttsx3.init()


import random

names = ["Snake", "Water", "Gun"]

random_name = random.choice(names)

# print("Randomly selected name:", random_name)
print("==== Snake    Water     Gun ====    ")
guess = input("Choose any of them = ")
guess1=guess.capitalize()

if(random_name==guess1):
 engine.say("Game is draw ")
 engine.runAndWait()
 print("Computer choosen item :", random_name)
 print("Your choosen item : ",guess1)

elif(random_name=="Snake" and guess1=="Water"):
  engine.say("You  loose ")
  engine.runAndWait()
  print("Computer choosen item :", random_name)
  print("Your choosen item : ",guess1)
  

elif(random_name=="Water" and guess1=="Snake"):
 engine.say("You  Win ")
 engine.runAndWait()
 print("Computer choosen item :", random_name)
 print("Your choosen item : ",guess1)
 

elif(random_name=="Snake" and guess1=="Gun"):
 engine.say("You  Win ")
 engine.runAndWait()
 print("Computer choosen item :", random_name)
 print("Your choosen item : ",guess1)
 
  

elif(random_name=="Gun" and guess1=="Snake"):
 engine.say("You  loose ")
 engine.runAndWait()
 print("Computer choosen item :", random_name)
 print("Your choosen item : ",guess1)
 

elif(random_name=="Water" and guess1=="Gun"):
 engine.say("You  loose ")
 engine.runAndWait()
 print("Computer choosen item :", random_name)
 print("Your choosen item : ",guess1)
 
  

elif(random_name=="Gun" and guess1=="Water"):
  engine.say("You  Win ")
  engine.runAndWait()
  print("Computer choosen item :", random_name)
  print("Your choosen item : ",guess1)

else:
 engine.say("Something went wrong ")
 engine.runAndWait()

 



  
