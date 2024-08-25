def secs_to_mins(secs:int)->str:
    minutes:int = int(secs/60)
    rem_secs:int = int(secs%60)
    return f"{secs} seconds is equals to {minutes} minutes and {rem_secs} seconds"

seconds = int(input("Enter Seconds to convert into minutes and seconds: "))
print(secs_to_mins(seconds))
