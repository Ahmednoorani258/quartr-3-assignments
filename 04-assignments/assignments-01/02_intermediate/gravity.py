MARS_MULTIPLE = 0.378  

def mars_weight_calculation():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)
    print("The equivalent weight on Mars: " + str(rounded_mars_weight))

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def planetary_weight_calculation():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY

    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)
    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight))

def main():
    print("Choose an option:")
    print("1. Calculate weight on Mars")
    print("2. Calculate weight on another planet")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        mars_weight_calculation()
    elif choice == "2":
        planetary_weight_calculation()
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
