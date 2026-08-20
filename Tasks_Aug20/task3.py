#Write a Python program to take distance in kilometer and convert it into meters, centimeters and milimeters

distance_in_kilometers = float(input("Enter distance in kilometers: "))
distance_in_meters = distance_in_kilometers*1000
distance_in_centimeters = distance_in_meters*100
distance_in_millimeters = distance_in_centimeters*10

print("Distance in kilometers:", distance_in_kilometers,
      "\nDistance in meters:", distance_in_meters,
      "\nDistance in centimeters:", distance_in_centimeters,
      "\nDistance in millimeters:", distance_in_millimeters)