# TASK 5: Creating an object named Boeing.
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
print("\nInitial coordinates of airplane1:", a1.x,a1.y)
a1.moveright()
a1.movedown()
print("Final coordinates of airplane1:",a1.x,a1.y)

a2 = aircraft(1, 2)
print("\nInitial coordinates of airplane1:", a2.x, a2.y)
a2.movedown()
a2.moveleft()
print("Final coordinates of airplane2:",a2.x,a2.y)

a3 = aircraft(4, 3)
print("\nInitial coordinates of airplane1:", a3.x, a3.y)
a3.moveup()
a3.moveright()
print("Final coordinates of airplane3:",a3.x,a3.y)

a4 = aircraft(5, 3)
print("\nInitial coordinates of airplane1:", a4.x, a4.y)
a4.movedown()
a4.moveleft()
print("Final coordinates of airplane4:",a4.x,a4.y)

a5 = aircraft(2, 2)
print("\nInitial coordinates of airplane1:", a5.x, a5.y)
a5.moveup()
a5.moveright()
print("Final coordinates of airplane5:",a5.x,a5.y)

class Boeing(aircraft):
    def __init__(a, x, y,x_d,y_d):
        a.x = x
        a.y = y
        a.x_d = x_d
        a.y_d = y_d


a1 = Boeing(12,36,23,45)
print("\nInitial coordinates of Boeing 1:", a1.x,a1.y)
a1.moveright()
a1.movedown()
print("Final coordinates of Boeing 1:",a1.x_d,a1.y_d)


a2 = Boeing(4,100,33,99)
print("\nInitial coordinates of Boeing 2:", a1.x,a1.y)
a2.movedown()
a2.moveleft()
print("Final coordinates of Boeing 2:",a2.x_d,a2.y_d)


a3 = Boeing(23,42,1,66)
print("\nInitial coordinates of Boeing 3:", a1.x,a1.y)
a3.moveup()
a3.moveright()
print("Final coordinates of Boeing 3:",a3.x_d,a3.y_d)


a4 = Boeing(67,12,56,81)
print("\nInitial coordinates of Boeing 4:", a1.x,a1.y)
a4.movedown()
a4.moveleft()
print("Final coordinates of Boeing 4:",a4.x_d,a4.y_d)

a5 = Boeing(9,33,2,67)
print("\nInitial coordinates of Boeing 5:", a1.x,a1.y)
a5.moveup()
a5.moveright()
print("Final coordinates of Boeing 5:",a5.x_d,a5.y_d)





