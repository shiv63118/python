print("Enter 1 to select celsius scale for your input.\nEnter 2 to select fahrenheit scale for your input.\nEnter 3 to select kelvin scale for your input.")

choice = int(input("Choose your input scale : "))
if choice == 1:
    print("Your choice is celsius..")
    celsius = float(input("Enter your temperature in celsius : "))
    print(f"{celsius} celsius = {1.8*celsius+32} fahrenheit")
    print(f"{celsius} celsius = {celsius+273.15} kelvin")
    
elif choice == 2:
    print("Your choice is fahrenheit..")
    fahrenheit = float(input("Enter your temperature in fahrenheit : "))
    print(f"{fahrenheit} fahrenheit = {((fahrenheit-32)*5)/9} celsius")
    print(f"{fahrenheit} fahrenheit = {((fahrenheit-32)*5)/9+273.15} kelvin")
    
elif choice == 3:
    print("Your choice is kelvin..")
    celsius = float(input("Enter your temperature in kelvin : "))
    print(f"{kelvin} kelvin = {kelvin-273.15} celsius")
    print(f"{kelvin} kelvin = {(kelvin-273.15)*1.8+32} fahrenheit")
    
else: 
    print(f"{choice} is not a valid choice. (choose among 1 2 3)")