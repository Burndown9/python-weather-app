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


API KEY: 4861192b2ae379f9b65947707449278c
"""

#version 2.2

#------------------------------------------------------------------------#
################################DEPENDENCIES##############################
#------------------------------------------------------------------------#

                    #city.list.json (not yet implemented)
                    #This solution will contain a city.list.json file that it relies on to convert cities to City IDs

#------------------------------------------------------------------------#
##################################IMPORTS#################################
#------------------------------------------------------------------------#

import json #to convert cities to City IDs
#import re #to check string mask
import requests #to request data from OpenWeatherMaps
import uszipcode #to convert zip codes to latitude and longitude

#------------------------------------------------------------------------#
##################################CLASSES#################################
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
#################################FUNCTIONS################################
#------------------------------------------------------------------------#
def K_to_C(k):
    return (k - 273.15)

def C_to_F(c):
    return (c * 9 / 5 + 32)


def Get_Weather(zip_or_city):
    #This function will use the OpenWeatherMap API to send a City ID and retrieve a weather forecast.
    #Then it will display the forecast to the user's screen.
    #OpenWeatherMap requests calls to its API be done by City ID instead of city name or zip code.
    #This function first checks to see if it was given a zip code or a city name, then attempts to correlate that with an existing City ID
    #If it cannot, it will alert the user about a failure to connect.

    const_APP_ID = "4861192b2ae379f9b65947707449278c"

    try:
        #Check to see if the string input is able to be converted to a zip code (that is, it is five digits):
        #########is_zip_code = re.match([0-9][0-9][0-9][0-9][0-9], zip_or_city)
        is_zip_code = zip_or_city.isdigit()
        #if so, use uszipcode to convert it to latitude and longitude
        if is_zip_code:
            search = uszipcode.SearchEngine()
            zipcode = search.by_zipcode(zip_or_city)
            lat = zipcode.lat
            lon = zipcode.lng
            #use the latitude and longitude in an API call to OpenWeatherApp
            #api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID=4861192b2ae379f9b65947707449278c
            parameters = {
                "lat": lat,
                "lon": lon,
                "APPID": const_APP_ID
                }
            Print_Weather(parameters)

        else:
        #if not a zip code, check to see if it matches a city
            #with open('city.list.json') as city_json:
                #data = json.load(city_json)
            
        #I couldn't get the city list json file to work with python, as it doesn't match the syntax of json files I see when attempting to look up
        #solutions. For the time being, I will just send the city name in the API call, and attempt to add cityID support later
            parameters = {
                "q": zip_or_city,
                "APPID": const_APP_ID
                }

            Print_Weather(parameters)
    except:
        print("There was an issue retrieving your weather information. Please try again later.")

    
def Print_Weather(parameters):
    try:
            #get weather
            weather_response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameters)
            if (weather_response.status_code == 404):
                raise NotFoundError
            data = weather_response.json()

            #-----#
            city = data["name"]
            weather = data["weather"][0]["main"]
            temp_c = K_to_C(data["main"]["temp"])
            temp_f = C_to_F(temp_c)
            #-----#
            print("Weather right now in " + city + ": " + weather + " with a temperature of " + str(round(temp_c)) + " degrees C (" + str(round(temp_f)) 
                  + " degrees F).")

            #get forecast
            #api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID=4861192b2ae379f9b65947707449278c
            weather_response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
            data = weather_response.json()
            #print(json.dumps(data, indent=4))
            Forecast(data, 5)
            Forecast(data, 13)
            Forecast(data, 21)
            Forecast(data, 29)


    except:
        print("Your weather data was unable to be found. Please double-check your input and try again.")

def Forecast(data, hour):
    dt = data["list"][hour]["dt_txt"][:10]
    dweather = data["list"][hour]["weather"][0]["main"]
    dtemp = data["list"][hour]["main"]["temp"]

    print("Weather on " + dt + " will be " + dweather + " with a temperature of " + str(round(K_to_C(dtemp))) + 
                  " degrees C at noon (" + str(round(C_to_F(K_to_C(dtemp)))) + " degrees F)")

#------------------------------------------------------------------------#
###################################MAIN###################################
#------------------------------------------------------------------------#
def main():
    while 1: #infinite loop allows the user to run the program multiple times
        print("""Welcome to the
      ____        _   _                  __        __         _   _                    _                
     |  _ \ _   _| |_| |__   ___  _ __   \ \      / /__  __ _| |_| |__   ___ _ __     / \   _ __  _ __  
     | |_) | | | | __| '_ \ / _ \| '_ \   \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|   / _ \ | '_ \| '_ \ 
     |  __/| |_| | |_| | | | (_) | | | |   \ V  V /  __/ (_| | |_| | | |  __/ |     / ___ \| |_) | |_) |
     |_|    \__, |\__|_| |_|\___/|_| |_|    \_/\_/ \___|\__,_|\__|_| |_|\___|_|    /_/   \_\ .__/| .__/ 
            |___/                                                                          |_|   |_|    """)
        zip_or_city = input("Please enter your 5 digit zip code or city name for a weather forecast: ")
        Get_Weather(zip_or_city)

        #ask the user if they'd like to continue the program
        again = input("Enter Y to get another forecast, or anything else to quit ")
        if (again == "Y" or again == "y"): #if they entered anything other than "y" or "Y"
            pass
        else:
            break



if (__name__ == "__main__"):
    main()

