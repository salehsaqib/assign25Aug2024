def calculate_age(bYear:int)->int:
    currentYear:int = 2024
    age:int = currentYear - bYear
    return age

birthYear:int = int(input("Enter Your Birth Year: "))
print(f"Your age is : {calculate_age(birthYear)}")

