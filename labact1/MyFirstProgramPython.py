#Casa,Aldwin Keith D. BSCS 1B

#weight to kilograms
pounds = eval(input("Weight in Pounds (lbs):"))
conversion = 2.205
kilograms = (pounds) / (conversion)
print("Weight converted to Kilograms (km):",kilograms)
print("=====================================================")
#leght to kilometer
Miles = eval(input("Lenght in Miles (mi):"))
conversion = 1.609344
kilometers = (Miles) * (conversion)
print("Lenght converted to Kilometers (km):",kilometers)
print("=====================================================")
#fahrenhiet to celsius
F = eval(input("Temperature in Fahrenheit (°F):"))
conversion = -32
Fahrenheit = (F - 32) * 5/9
print("Temperature in Celsius (°C) =",Fahrenheit)
print("=====================================================")
#average of the numbers
a = eval(input("Age of the student 1:"))
b = eval(input("Age of the student 2:"))
c = eval(input("Age of the student 3:"))
d = eval(input("Age of the student 4:"))
e = eval(input("Age of the student 5:"))
f = eval(input("Age of the student 6:"))
g = eval(input("Age of the student 7:"))
h = eval(input("Age of the student 8:"))
i = eval(input("Age of the student 9:"))
j = eval(input("Age of the student 10:"))
add = a+b+c+d+e+f+g+h+i+j
avg = add / 10
print("The average age of the student is:", avg)
print("====================================================")

character1 = "MK.R"
item1 = "Jupiter Assault Riffle"
ability1 = "Triple Rocket launcher"

character2 = "Maggie"
ability2 = "Taktical Roll"

character3 = "Ceanna"
ability3 = "Retoration Field"

character4 = "Phantom"
ability4 = "Sniper Fatal Head Shot"





story= f"""
The Farlight ground Base in Earth 2.0, there is a constructed spacecraft going home covered with high walls and heroes.
Suddenly there was a loud bang <{ability1} boowmm>, destroying the wall of the base.
The base is under attack by troops of robots under {character1} that has a rapid gun <{item1}> that can destroy everything.
Everything on their front was destroyed and getting closer, but the heroes came and protected the spacecraft.
Here comes {character2} who has a jetpack boost and reloads her gun instantly, <{ability2} goess brrr> that dominates half of the troops.
Suddenly she got shot but it didn't kill her, thanks to {character3} her friend who deployed a device recovery<{ability3}> that can provide healing and shield repair 
and has a drone that shoots, but suddenly they got wasted by {character1}.
While {character1} is busy with them, {character4} their sniper friend takes a shot at his head <{ability4} go boom> from the distance that,
makes all enemy troops shut down and protects the spacecraft going home to the real Earth.
"""
print(story)




