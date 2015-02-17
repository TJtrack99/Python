print "Blackjack program"
cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
import random
flag = 1
while(flag==1):
  draw = random.randint(0, 52)-1
  
