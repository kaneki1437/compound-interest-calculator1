principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("Principle amount cant be less than 0")
print(principle)
while rate <= 0:
    rate = float(input("Enter the interest rate:"))
    if rate <= 0:
        print("Interest rate cant be less than 0")
while time <= 0:
    time = int(input("Enter the time in years:"))
    if time <= 0:
        print("Time cant be less than 0")
total = principle * pow((1 + rate / 100), time)
print(f"balance after {time} year/s: ${total:.2f}")


