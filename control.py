import requests
from pprint import pprint
import datetime
from helper import D
from weather import weather_reporter

class Oikia:
    
    def __init__(self,D):
        self.D = D
        self.weather_reporter = weather_reporter
        
    def menu(self):
        print("What would you like to do??")
        print("Enter 1 to see 24-hour weather report")
        user_input = input()
        if user_input == 1:
            pprint(self.weather_reporter(D=self.D))
        else:
            print("idk")
            
        # need a quit option
        
        
def main():
    
    o = Oikia(D=D)
    o.menu()
        
if __name__ == "__main__":
    
    main()
    
    