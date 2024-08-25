def circleArea(r:int)->float:
    PI:float = 22/7
    area:float =  round((PI * r*r),2)
    return area
    
rd:int = int(input("Enter Radius for a circle: "))
print(f"Area of circle is :{circleArea(rd)}")
