def find_bmi(user_weight:float, user_height:float)->float:
    userBMI:float = float(user_weight/(user_height*user_height))
    return round(userBMI,2)

userWt = float(input("Enter Weight in Kgs: "))
userHt = float(input("Enter Height in meters: "))
print(f"Your BMI is: {find_bmi(userWt,userHt)}")

