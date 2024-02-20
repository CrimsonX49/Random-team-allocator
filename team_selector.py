import random

print("Welcome to the random team allocator!")

print("\n")

players = ["Martin", "Craig", "Sue", 
           "Claire", "Dave", "Alice",
           "Lucy", "Harry", "Jack", 
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "Will", 
           "Ada", "Grace", "Jean", 
           "Marissa", "Alan", "Austin",
           "Mark", "John", "Walt", 
           "Sarah", "Barry", "Monica",
           "Natalie", "Shiri", "Charles"] 

random.shuffle(players)
    
team1 = players[:len(players)//3]
print("Team 1 Captain: " + random.choice(team1))
print("Team 1:")
for player in team1:
    print(player, end=" ")
print("\n")

team2 = players[len(players)//3:(len(players))//3*2]
print("Team 2 Captain: " + random.choice(team2))
print("Team 2:")
for player in team2:
    print(player, end=" ")
print("\n")

team3 = players[(len(players))//3*2:]
print("Team 3 Captain: " + random.choice(team3))
print("Team 3:")
for player in team3:
    print(player, end=" ")
print("\n")
