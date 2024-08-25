def cub_area(ed_len:int)->int:
    cubeArea:int = 6 * ed_len*ed_len
    return cubeArea
    

edgeLen = int(input("Enter length for the single edge: "))
print(f"Area of cube is :{cub_area(edgeLen)}")

