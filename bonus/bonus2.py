a = float(input("give me temperature in celsium\n"))
print("Fahrenheit:")
print(a*1.8+32)
print("Kelvin:")
print(a+273.15)

if a >= 35.5 and a < 37:
    print("You're healthy go home")
if a >= 37 and a < 38:
    print("Stay cool!")
if a >= 34 and a < 35.5:
    print("Stay warm!")
if a >= 25 and a < 34:
    print("It's pretty hot outside")
if a >= 10 and a < 25:
    print("I think your refrigerator's dying")
if a >= -35 and a < 10:
    print("You need your coat")
    if a < 0:
        print("And your gloves")
    if a < -10:
        print("And your hat")
    if a < -20:
        print("And your scarf")
    if a <= -25:
        print("Me too I hate this country")            
if a >= 38 and a < 40:
    print("You should seriously consider seeing a doctor")
if a >= 40 and a < 43:
    print("You know you're mortal right?")
if a >= 43 and a < 50:
    print("Seriously no idea why you would want to convert this temperature")
if a >= 50 and a < 60:
    print("Perfect tea temperature")
if a >= 60 and a < 80:
    
    print("Drinking tea this hot might increase your chances of esophagus cancer")
if a >= 80 and a < 280:
    print("I really hope this is the temperature in your oven")
if a > 280:
    print("You just typed a random number didn't you?")
if a < -30:
    print("bo-ring")

