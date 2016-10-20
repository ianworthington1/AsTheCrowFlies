#AsTheCrowFlies.py
__Author__ = "Ian Worthington D16124514"

#I couldn't figure our how to do the final question using no loops, so I
#compensated by making the user prompts absolutely ridiculous!
#Have fun!!

import time
from math import pi, cos, sin, acos


def toradians(degrees):                                                                                                 #converts all degrees into radians and returns
    radians = (degrees * ((2 * pi) / 360))
    return radians


def main():                                                                                                             #Stores main variables for the first iteration of the equation
    print("This production has been brought to you by", __Author__, "!!")
    time.sleep(.5)
    print("Welcome to PyAir! We hope you enjoy the maths we provide today!")
    time.sleep(2)
    print("On todays Maths adventure, we will be calculating the distance between locations")
    time.sleep(3)
    print("and airports using a variety of methods! Please fasten your fun-belts, and brace for impact!!")
    time.sleep(3)
    first_latitude = toradians(float(input("Please enter the first latitude coordinate")))
    print("Ah yes, a fine choice!")
    time.sleep(1.5)
    longitude1 = toradians(float(input("Please enter the first longitude coordinate")))
    print("Good sir, you seem to be a natural at typing! Well done indeed!")
    time.sleep(2)
    second_latitude = toradians(float(input("Please enter the second latitude coordinate")))
    print("Well, I do say, I AM impressed!")
    time.sleep(1.5)
    longitude2 = toradians(float(input("Please enter the second longitude coordinate")))
    print("A brilliant final choice, sir, if I do say so myself!")
    time.sleep(1.5)
    distance = distance_between_points(first_latitude, longitude1, second_latitude, longitude2)
    print("%.2f" % distance, "km")
    time.sleep(1)
    proceed1()


def distance_between_points(first_latitude, longitude1, second_latitude, longitude2):                                   # Breaks down the equation into more manageable sections
    Sin_val = (sin((toradians(90)) - first_latitude)) * (sin((toradians(90)) - second_latitude))
    Cos_val = (cos(longitude1 - longitude2))
    right_side = (cos((toradians(90)) - first_latitude)) * (cos((toradians(90)) - second_latitude))
    left_side = Sin_val * Cos_val

    distance = acos((left_side) + (right_side)) * 6371
    return distance

def proceed1():
    user_prompt1 = str(input("Would you like to proceed to the Distance Table? y/n"))
    if user_prompt1 == "y":
        distance_table()
    elif user_prompt1 == "n":
        end()


def distance_table():

    Airports = [                                                                                                        #Defines a list of Dictionaries for the Airports and their coordinates
        {'Code': "DUB", 'Airport': "Dublin", 'Latitude': 53.421333, 'Longitude': -6.270075},
        {'Code': "LHR", 'Airport': "London-Heathrow", 'Latitude': 51.4775, 'Longitude': -0.461389},
        {'Code': "JFK", 'Airport': "John F Kennedy Intl", 'Latitude': 40.639751, 'Longitude': -73.778925},
        {'Code': "AAL", 'Airport': "Aalborg", 'Latitude': 57.092789, 'Longitude': 9.849164},
        {'Code': "CDG", 'Airport': "Charles de Gaulle", 'Latitude': 49.012779, 'Longitude': 2.55},
        {'Code': "SYD", 'Airport': "Sydney", 'Latitude': -33.946111, 'Longitude': 151.177222}
    ]
    time.sleep(1)
    print("\n")
    print("And here. We. GOOOOOOoooooooo!")
    for d in Airports:                                                                                                  #start a loop for every dictionary entry in the Airport list
        print("")
        print("From", d['Airport'], "to :")
        time.sleep(.5)                                                                                                  #Used so that the table when printed does not need to be scrolled through! Makes it nicer to follow the print of info
        getdistlatitude1 = toradians(d['Latitude'])                                                                     #\
        getdistlongitude1 = toradians(d['Longitude'])                                                                   #-  Stores new variables
        for d in Airports:                                                                                              #start a loop within the main loop for every entry within the airport list
            getdistlatitude2 = toradians(d['Latitude'])                                                                 #\
            getdistlongitude2 = toradians(d['Longitude'])                                                               #- Stores new variables
            distance = distance_between_points(getdistlatitude1, getdistlongitude1, getdistlatitude2, getdistlongitude2)#^^ runs the distance_between_points equation with the newly stored values
            time.sleep(.5)                                                                                              #Same reason as the first time.sleep function: Just makes it nicer to watch!
            print(d['Airport'],":", "%.2f" %distance, "km")                                                            #Prints things all pretty!!
        time.sleep(.5)                                                                                                  #As the others before it!
    time.sleep(.5)
    print("\n")
    time.sleep(1)
    proceed2(Airports)


def proceed2(Airports):
    user_prompt2 = str(
        input("Would you like to proceed to get the distance between Airports using respective Airport Codes? y/n"))
    if user_prompt2 == "y":
        getDistancebetweenAirports(Airports)
    elif user_prompt2 == "n":
        end()


def getDistancebetweenAirports(Airports):
    ask_user1 = str(input("What airport would you like to start with? (Please remember to use block capitols i.e, HIT CAPS LOCK NOW!)"))
    ask_user2 = str(input("What airport would you like to measure to? (Please remember to use block capitols i.e, HIT CAPS LOCK NOW!)"))

    for check in range(0, 6):
        airport = Airports[check].get('Code')
        if ask_user1 == airport:
            newlat1 = toradians(Airports[check].get('Latitude'))
            newlong1 = toradians(Airports[check].get('Longitude'))
            AirName1 = Airports[check].get('Airport')
        if ask_user2 == airport:
            newlat2 = toradians(Airports[check].get('Latitude'))
            newlong2 = toradians(Airports[check].get('Longitude'))
            AirName2 = Airports[check].get('Airport')

    mango = distance_between_points(newlat1, newlong1, newlat2, newlong2)
    print("From ", AirName1, " to ", AirName2 , "is a distance of: ", "%.2f" %mango, "km")

    end()


def end():                                                                                                              #Just for fun
    time.sleep(1)
    print("")
    time.sleep(.5)
    print("Cu-Caw!")
    time.sleep(.5)
    print("Thank you for flying with PyAir! We hope you had some nice maths!")
    time.sleep(1)


main()