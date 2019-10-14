# TASK 3: Created a class with 5 instances
# Maneuvering the 5 aircrafts and then printing their coordinates.

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


a1 = aircraft()
a2 = aircraft()
a3 = aircraft()
a4 = aircraft()
a5 = aircraft()

y1 = a1.moveright()
x1 = a1.movedown()
print("\ncoordinates of airplane1:",a1.x,a1.y)

y2 = a2.movedown()
x2 = a2.moveleft()
print("\ncoordinates of airplane2:",a2.x,a2.y)

y3 = a3.moveup()
x3 = a3.moveright()
print("\ncoordinates of airplane3:",a3.x,a3.y)

y4 = a4.movedown()
x4 = a4.moveleft()
print("\ncoordinates of airplane4:",a4.x,a4.y)


y5 = a5.moveup()
x5 = a5.moveright()
print("\ncoordinates of airplane5:",a5.x,a5.y)








