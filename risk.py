print "Risk results"
flag = 1
while(flag==1)
  attack = input("Input number of attackers:")
  if attack>3:
    attack=3
  defend = input("Input number of defenders:")
  if defend>2:
    defend=2
  import random
  die1=random.randint(0, 6)
  die2=random.randint(0, 6)
  if(die1>=die2):
    greatestA = die1
    2greatestA = die2
  else:
    greatestA = die2
    2greatestA = die1
  die3=random.randint(0, 6)
  if(die3>=greatest):
    2greatestA=greatest
    greatestA=die3
  else if(die3>=2greatest):
    2greatestA=die3
  print "Attackers: Rolls of " + die1 + " and " + die2 + " and " + die3
  die1=random.randint(0, 6)
  die2=random.randint(0, 6)
  if(die1>=die2):
    greatestD = die1
    2greatestD = die2
  else:
    greatestD = die2
    2greatestD = die1
  print "Defenders: Rolls of " + die1 + " and " + die2
  if(greatestD>=greatestA AND 2greatestD>=greatestA):
    print "Defenders win twice"
  else if((greatestD>=greatestA AND 2greatestD<greatestA) OR (greatestD<greatestA AND 2greatestD>=2greatestA)):
    print "Each lose one"
  else if(greatestD<greatestA AND 2greatestD<2greatestA):
    print "Attackers win twice"
  else:
    print "Invalid"
  flag = input("Continue? Type 1 for yes, 0 for no")
