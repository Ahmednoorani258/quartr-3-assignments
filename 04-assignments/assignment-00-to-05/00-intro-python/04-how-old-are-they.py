def main():
    anton : int = 21
    beth : int = 6 + anton 
    chen : int = 20 + beth 
    drew  : int= chen + anton
    ethan : int = chen

    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()