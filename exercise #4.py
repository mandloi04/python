# TASK 4: Created a class with 5 instances and giving the coordinates.
class aircraft:


    def __init__(a,x,y):
        a.x = x
        a.y = y

    def moveup(a):
        a.y = a.y + 1

    def moveleft(a):
        a.x = a.x - 1

    def moveright(a):
        a.x = a.x + 1

    def movedown(a):
        a.y = a.y - 1

a1 = aircraft(0,0)
a2 = aircraft(1,2)
a3 = aircraft(4,3)
a4 = aircraft(5,3)
a5 = aircraft(2,2)

a1.moveright()
a1.movedown()
print("\ncoordinates of airplane1:",a1.x,a1.y)

a2.movedown()
a2.moveleft()
print("\ncoordinates of airplane2:",a2.x,a2.y)

a3.moveup()
a3.moveright()
print("\ncoordinates of airplane3:",a3.x,a3.y)

a4.movedown()
a4.moveleft()
print("\ncoordinates of airplane4:",a4.x,a4.y)


a5.moveup()
a5.moveright()
print("\ncoordinates of airplane5:",a5.x,a5.y)

