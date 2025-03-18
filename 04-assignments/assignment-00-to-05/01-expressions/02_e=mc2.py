def mass_to_energy(mass):
    energy = mass * 299792458 ** 2
    return energy

def main():
    user_input = float(input("Enter the mass in kilograms: "))
    energy = mass_to_energy(user_input)
    print("The energy is:", energy, "Joules")
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()