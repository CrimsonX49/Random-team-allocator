import random

print("Welcome to the Team allocator!")

players = ["Martin", "Craig", "Sue", 
           "Claire", "Dave", "Alice",
           "Lucy", "Harry", "Jack", 
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "Will", 
           "Ada", "Grace", "Jean", 
           "Marissa", "Alan"] 

random.shuffle(players)
team1 = players[:len(players)//2]
print("Team 1 Captain: " + random.choice(team1))
print("Team 1:")
for player in players:
    print(player)