# TASK2: Creating a class named aircraft. Maneuvering the aircraft and printing the coordinates of the aircraft


class aircraft:
    x=0
    y=0
    acc=1


    def moveup(a):
        a.y = a.y + 1

    def moveleft(a):
        a.x = a.x-1


    def moveright(a):
        a.x = a.x + 1


    def movedown(a):
        a.y = a.y - 1
        

a = aircraft()

for i in range(2):
    a.moveleft()


for i in range(4):
    a.moveup()


for i in range(2):
    a.movedown()


for i in range(4):
    a.moveright()

print("Coordinates in x-plane:",a.x)
print("Coordinates in y-plane:",a.y)

	