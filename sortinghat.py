#harry potter sorting hat

slytherin = 0
hufflepuff = 0
ravenclaw = 0
gryffindor = 0

q1 = int(input("Do you like 1) dusk or 2) dawn?"))

if q1 == 1:
  gryffindor = 1 
  ravenclaw = 1
elif q1 == 2:
  hufflepuff = 1
  slytherin = 1
else:
  print("Wrong input.")

q2 = int(input("When I'm dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold"))

if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print("Wrong input.")

q3 = int(input("Which kind of instrument most please your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum"))

if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print("Wrong input.")

print("Slytherin: ", slytherin, "Hufflepuff: ", hufflepuff, "Ravenclaw: ", ravenclaw, "Gryffindor: ", gryffindor)
