#(5 points): As a developer, I want to make at least three commits with descriptive messages 
#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10  points): As a user, I want to display my completed trip in the console
#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 

import random

Intro_message = "Welcome to the Day Trip Calculator, If you do not know what do to for a day trip you have come to the right place, I will help you select your trip."
print( Intro_message)


#List of Destinations
trip_destinations = ['America', 'Mexico', 'Japan', 'Peru', 'Russia']
#List of restraunts
trip_restaurants = ['Joes', 'El Taco', 'Mt Fuji','El Turt', 'Bequiro']
#list of transportation
trip_transport = ['Plane', ' Car', 'Train','Walking','Scootering']
#list of entertainment
trip_entertainment = ['Hiking', 'Shopping', 'Shrining',' Fishing','Surfing']



# Randomators
destination = random.choice(trip_destinations)
restaurant = random.choice(trip_restaurants)
transportation = random.choice(trip_transport)
entertainment = random.choice(trip_entertainment)

confirm = input('Please type y to start and y/n to confirm your travel option. ')

# Function for destination
def new_destie(confirm):  
    while confirm == 'y':
            destination = random.choice(trip_destinations)
            confirm = input(f'We have seleceted {destination} as your trip destination. Would you prefer to travel somewhere else?(y/n) ')
    if confirm == 'y':
        True
    else:
        print(f'Glad you selected {destination} as the destination for your trip. ')

new_destie(confirm)

def foodie_yum(confirm):  
    while confirm == 'y':
            restaurant = random.choice(trip_restaurants)
            confirm = input(f'We have seleceted {restaurant} as your place to grab a bite. Would you prefer a different local restaurant?(y/n) ')
    if confirm == 'y':
        True
    else:
        print(f'YUM! Glad you selected {restaurant} as the restaurant for your trip. ')

foodie_yum(confirm)

def lift_glide(confirm):
    while confirm == 'y':
            transportation = random.choice(trip_transport)
            confirm = input(f'We have seleceted {transportation} as your mode of transportation. would you prefer something else?(y/n) ')
    if confirm == 'y':
        True
    else:
        print(f'Zoom! Glad you selected {transportation} as the method of movement for your trip. ')

lift_glide(confirm)

def entertain(confirm):
    while confirm == 'y':
            entertainment = random.choice(trip_entertainment)
            confirm = input(f'We have seleceted {entertainment} as your option for fun on the trip. would you prefer to do something else?(y/n) ')
    if confirm == 'y':
        True
    else:
        print(f'PARTY ROCKING IN THE HOUSE TONIGHT! Glad you selected {entertainment} as your choice of entertainment! ')

entertain(confirm)

print(f'Enjoy your trip to {destination} we hope the food is to your liking at {restaurant}. Do not forget to grab your pass for the {transportation} on your way to go {entertainment}.')






