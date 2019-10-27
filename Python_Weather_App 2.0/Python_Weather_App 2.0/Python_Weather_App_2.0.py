"""
Name: Python Weather App
Programmer: Jacob Hayes
Date: 07 Sept 2019 - 
Purpose: Your program must prompt the user for their city or zip code and request weather forecast data from openweathermap.org.
         Your program must display the weather information in an READABLE format to the user.
"""

"""
REQUIREMENTS
Create a Python Application which asks the user for their zip code or city.
Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
Display the weather forecast in a readable format to the user.
Use comments within the application where appropriate in order to document what the program is doing.
Use functions including a main function.
Allow the user to run the program multiple times.
Validate whether the user entered valid data.  If valid data isn’t presented notify the user.
Use the Requests library in order to request data from the webservice.
Use Python 3.
Use try blocks when establishing connections to the webservice.  You must print a message to the user indicating whether or not the connection was successful.
"""

#------------------------------------------------------------------------#
################################DEPENDENCIES##############################
#------------------------------------------------------------------------#

#city.list.json
#This solution contains a city.list.json file that it relies on to convert cities to City IDs

#------------------------------------------------------------------------#
##################################IMPORTS#################################
#------------------------------------------------------------------------#

import json #to convert cities to City IDs
import requests #to request data from OpenWeatherMaps 

#------------------------------------------------------------------------#
##################################CLASSES#################################
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
#################################FUNCTIONS################################
#------------------------------------------------------------------------#

def Get_Weather(zip_or_city):
    #This function will use the OpenWeatherMap API to send a City ID and retrieve a weather forecast.
    #Then it will display the forecast to the user's screen.
    city_ID = Convert_to_City_ID(zip_or_city)

def Convert_to_City_ID(zip_or_city):
    #OpenWeatherMap requests calls to its API be done by City ID instead of city name or zip code.
    #This function first checks to see if it was given a zip code or a city name, then attempts to correlate that with an existing City ID
    #If it cannot, it will alert the user about a failure to connect.
    pass

#------------------------------------------------------------------------#
###################################MAIN###################################
#------------------------------------------------------------------------#

while 1: #infinite loop allows the user to run the program multiple times
    print("""Welcome to the
  ____        _   _                  __        __         _   _                    _                
 |  _ \ _   _| |_| |__   ___  _ __   \ \      / /__  __ _| |_| |__   ___ _ __     / \   _ __  _ __  
 | |_) | | | | __| '_ \ / _ \| '_ \   \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|   / _ \ | '_ \| '_ \ 
 |  __/| |_| | |_| | | | (_) | | | |   \ V  V /  __/ (_| | |_| | | |  __/ |     / ___ \| |_) | |_) |
 |_|    \__, |\__|_| |_|\___/|_| |_|    \_/\_/ \___|\__,_|\__|_| |_|\___|_|    /_/   \_\ .__/| .__/ 
        |___/                                                                          |_|   |_|    """)
    zip_or_city = input("Please enter your zip code or city for a weather forecast: ")
    Get_Weather(zip_or_city)

    #ask the user if they'd like to continue the program
    again = input("Enter Y to get another forecast, or anything else to quit ")
    if (again.upper != "Y"): #if they entered anything other than "y" or "Y"
        #quit the program
        break

