#GPA Calculator
#Shane Tappa
#7/30/17

def rectangle_calc():
    height = 0.0
    width = 0.0
    area = 0.0
    
    while True:
        try:
            height = float(raw_input("Enter the height of your rectangle: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    while True:
        try:
            width = float(raw_input("Enter the width of your rectangle: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    area = height * width
    
    print "The area of your rectangle is: {:,.2f}".format(area)
    
def right_triangle_calc():
    base = 0.0
    height = 0.0
    area = 0.0
    
    while True:
        try:
            base = float(raw_input("Enter the base of your right rectangle: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    while True:
        try:
            height = float(raw_input("Enter the height of your right rectangle: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    area = 0.5 * base * height
    
    print "The area of your right rectangle: {:,.2f}".format(area)
    
def circle_calc():
    import math
    radius = 0.0
    area = 0.0
    
    #print "Enter the radius of your circle:"
    #radius = float(raw_input())
    while True:
        try:
            radius = float(raw_input("Enter the radius of your circle: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    area = 4*math.pi*radius**2
    print "The area of your circle is: {:,.2f}".format(area)
    
choice = 0
print "Welcome to the geometry calculator"
print "Your choices are:" 
print "1 = rectangule calculator, 2 = right triangle calculator" 
print "3 = circle calculator, 4 = quit program"
print "Choose the shape whose area you want to calculate."
#choice = raw_input() 
#choice = int(choice) 

while True:
    try:
        choice = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
                       
while choice != 4:     
    if choice == 1:
        print "Your choice was: %s" % choice + " (rectangle calculator)"  
        rectangle_calc()
    elif choice == 2:
        print "Your choice was: %s" % choice + " (right triangle calculator)"  
        right_triangle_calc()
    elif choice == 3:
        print "Your choice was: %s" % choice + " (circle calculator)"  
        circle_calc()
    print ""
    print "Choose another shape whose area you want to calculate."
    print "1 = rectangule calculator, 2 = right triangle calculator" 
    print "3 = circle calculator, 4 = quit program"
    
    while True:
        try:
            choice = int(raw_input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
