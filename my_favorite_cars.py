#Kenneth Smith 4-21-2024 6.2

# A list of my favorite vehicles
myFavoriteCars = ("2015 Shelby GT350R",
                 "2024 Porsche 911 GT3",
                 "1998 Toyota Supra", 
                 "1999 Mitsubishi Eclipse",
                 "1999 Mazda RX-7",
                 "2014 Ford Mustang GT",
                 "1992 Nissan Skyline",
                 "1992 Ford Mustang GT", 
                 "2006 Chevrolet Corvette Z06",
                 "1969 Dodge Charger RT",
                 "1995 Nissan 240sx",
                 "2017 Dodge Viper ACR", 
                 "2022 Ford GT", 
                 "2015 Ford Mustang GT",
                 "2005 Honda NSX", 
                 "2022 Tesla Plaid",
                 "2024 Chevrolet Camaro ZL1", 
                 "1995 Eagle Talon", 
                 "2021 Audi R8",
                 "Tesla Model 3"
                 )

#Display the contents
print("My Favorite Cars:")
print(f"{myFavoriteCars}")
print()

#Iterate through the collection displaying the output as a complete sentence using each value. 
for car in myFavoriteCars:
    print(f"My favorite car is the {car}.")
print()

#Repeat the output in reverse order.
print("My Favorite cars in reverse order:")
for car in reversed(myFavoriteCars):
    print(f"My favorite car is the {car}.")