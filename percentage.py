def cal_per(amt:int,per:int)->str:
    answer:int =  int(amt * per/100)
    return f"{per}% of {amt} is :{answer}"

print(cal_per(int(input("Enter amount: ")),int(input("Enter Percentage to calculate: "))))
