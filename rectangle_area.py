def rect_area(len:int,wid:int)->str:
    area:int =  len * wid
    return f"Area of rectangle is :{area}"

print(rect_area(int(input("Enter length for a rectangle: ")),int(input("Enter width for a  rectangle: "))))
