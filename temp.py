def conv_temp(cen_temp:int, fah_temp:int)->str:
    F:float = float(cen_temp * (9/5) + 32)
    C:float = float((fah_temp - 32) * 5/9)
    return f"{cen_temp} in Fahrenheit: {round(F,2)} \n {fah_temp} in Centigrade: {round(C,2)}"

centi:int = int(input("Enter Temperature in Centigrade: "))
fahren:int = int(input("Enter Temperature in Fahrenheit: "))
print(conv_temp(centi, fahren))