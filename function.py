#!/usr/bin/python3

def main():
    #get temperature and wind speed from user
    temperature = float(input("Enter the temperature: "))
    speed = float(input("Enter the wind speed: "))

    #call function to calculate wind chill
    wChill = windChill(temperature,speed)

    #output temperature with wind chill
    print("The temperature with the wind chill is: ", wChill)

#function to calculate wind chill
def windChill(temp, speed):
    chill = 35.74 + 0.6215 * temp - 35.75 * (speed ** 0.16) + 0.4275 * temp 

    (speed ** 0.16)
    return chill

if __name__ == "__main__": main()
