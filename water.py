x = 0
y = 0
A = 4 
B = 3

goal = int(input("Enter goal state for jug A: "))

actions = []

while not(x == 2 and y == 0) and not(y == 2 and x == 0):
    print(x, " ", y)
    rule = int(input("Enter Rule Number: "))
    if(rule == 1): #(X,Y | X<4) 1
        x = A
    elif(rule == 2): #	(X,Y |Y<3) 2
        y = B
    elif(rule == 3): #	(X,Y |X>0) 3
        x = 0
    elif(rule == 4): #	(X,Y | Y>0) 4
        y = 0
    elif(rule == 5): # (X,Y | X+Y>=3 ^X>0) 6
        x -= B - y
        y = B
    elif(rule == 6): # (X,Y | X+Y>=4 ^ Y>0) 5
        y -= A - x
        x = A
    elif(rule == 7): #	(X,Y | X+Y <=3^ X>0) 8
        y += x
        x = 0
    elif(rule == 8): # (X,Y | X+Y<=4 ^Y>0) 7
        x += y
        y = 0

    actions.append([x, y, rule])

print("State  | Rule")
for action in actions:
    print(action[0], " ", action[1], " | ", action[2])

