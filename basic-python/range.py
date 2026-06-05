
numbers = list(range(10,16))
squares = []
for value in range(1,5):
    squares.append(value*2)

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player.title())
    
# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print(friends_food)