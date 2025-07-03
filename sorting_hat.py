# Codedex Python Chapter 16 - Sorting Hat Exercise

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Welcome message
print("The Sorting Hat")
print("\nWelcome to Hogwarts School of Witchcraft and Wizardry.")
print("The hat decides which of the four Houses each first-year" +
      " student goes to based on their responses.\n")

# Question 1
print("Q1) Do you like Dawn or Dusk?")
print("\t1) Dawn")
print("\t2) Dusk")

choice = int(input("Enter your choice: "))

if choice == 1:
  gryffindor += 1
  ravenclaw += 1
elif choice == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Invalid input.")

# Question 2
print("Q2) When I'm dead, I want people to remember me as: ")
print("\t1) The Good")
print("\t2) The Great")
print("\t3) The Wise")
print("\t4) The Bold")

choice = int(input("Enter your choice: "))

if choice == 1:
  hufflepuff += 2
elif choice == 2:
  slytherin += 2
elif choice == 3:
  ravenclaw += 2
elif choice == 4:
  gryffindor += 2
else:
  print("Invalid input.")

# Question 3
print("Q3) Which kind of instrument most pleases your ear? ")
print("\t1) The violin")
print("\t2) The trumpet")
print("\t3) The piano")
print("\t4) The drum")

choice = int(input("Enter your choice: "))

if choice == 1:
  slytherin += 4
elif choice == 2:
  hufflepuff += 4
elif choice == 3:
  ravenclaw += 4
elif choice == 4:
  gryffindor += 4
else:
  print("Invalid input.")

# Print out score for all houses
print("Score")
print("\tGryffindor: ", gryffindor)
print("\tHufflepuff: ", hufflepuff)
print("\tRavenclaw: ", ravenclaw)
print("\tSlytherin: ", slytherin)

# Bonus, print out house with most points
house = max(gryffindor, hufflepuff, ravenclaw, slytherin)
print("The Sorting Hat has decided...")
if house == gryffindor:
  print("🦁 Gryffindor!")
elif house == hufflepuff:
  print("🦡 Hufflepuff!")
elif house == ravenclaw:
  print("🦅 Ravenclaw!")
else:
  print("🐍 Slytherin!")

