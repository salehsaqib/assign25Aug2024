def cal_vol(rd:int, ht:int)->float:
    PI:float = 22/7
    cVol:float = float(cyHt*PI*cyR*cyR)
    return round(cVol,2)

cyHt:int = int(input("Enter Height of Cylinder: "))
cyR:int = int(input("Enter Radius for Cylinder: "))
print(f"Volume of Cylinder: {cal_vol(cyR,cyHt)}")