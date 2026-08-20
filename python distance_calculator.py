# simple program to convert kilometers into miles

# constant variable for converting km to miles
km_to_miles_ratio = 0.621371

# ask user for the first distance in kilometers
user_km_input = float(input("Enter distance in kilometers: "))

# calculate the answer in miles
calculated_miles = user_km_input * km_to_miles_ratio

# show the output answer
print("Distance in miles:", calculated_miles)

# ask user if they want to try again
ask_to_repeat = input("Do you want to convert another distance? (yes/no): ")

# check if they typed yes
if ask_to_repeat == "yes":
    # ask for another distance input
    second_km_input = float(input("Enter distance in kilometers: "))
    
    # calculate miles again
    second_calculated_miles = second_km_input * km_to_miles_ratio
    
    # print the second result
    print("Distance in miles:", second_calculated_miles)
else:
    # end the program if they say anything other than yes
    print("Program ended.")