Print( "I have information for the following planets:\n")

print(" 1.Venus 2. Mars 3. Jupiter")
print(" 4.Saturn 5. Uranus 6. Neptune\n")

weight = 185
planet = 3

#if else statement is will be written below:

if target_planet in planet_gravities:
    relative_gravity = planet_gravities[target_planet]
    codey_weight_on_target = codey_weight * relative_gravity
    print(f"Your weight on planet {target_planet} is {codey_weight_on_target:.2f} kg.")
else:
    print("Invalid planet number. Please enter a number between 1 and 6.")
