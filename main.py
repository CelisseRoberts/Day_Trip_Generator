from cgi import print_arguments
import random
 

destinations = ['Las Vegas, NV', 'New York, NY', 'Puerto Rico', 'Orlando, FL', 'Los Angeles, CA']

transportation = [' a bus', 'a train', 'a plane', 'a rental car', 'a ship/boat/ferry']

restaurants = ['Brio Italian Grille', 'Dallas BBQ', 'Casita Miramar', 'Kres Chophouse', 'Water Grill Restaurant']

entertainment = ['attending a comedy show','going to a concert', 'going to a museum', 'taking a sightseeing tour around the city', 'visiting an amusement park']


def welcome_message():
    print("Welcome to the Day Trip Generator!")

welcome_message()



def restaurant_generator():
    valid_response = True 

    while valid_response == True:
     randomly_generated_choice = random.choice(restaurants)   



def destination_generator():
    valid_response = True
    
    while valid_response == True: 
        randomly_generated_choice = random.choice(destinations)
        user_input = input(f'We have choosen {randomly_generated_choice} for your day trip. Do you like this choice? Enter Y or N: ')
        if user_input == 'Y':
         print('Yaaaaaaaay! Great choice!')  
         return randomly_generated_choice
        #  input(f'We selected {transportation} as your form of transporation today. Do you like this choice? Enter Y or N: ')
        
        elif user_input == 'N':
         print('Okay, we will try something else!')
         continue
        
        else: 
         print('Please select Y or N.')
         continue

  
         
choosen_destination = destination_generator()  

def transportation_generator():
    valid_response = True

    while valid_response == True: 
        randomly_generated_choice = random.choice(transportation)   
        user_input = input(f'You will be taking {randomly_generated_choice} for todays trip. Do you like this choice? Enter Y or N: ') 
        
        if user_input == 'Y':
         print('Yaaaaaaaay! Great choice!')
         return randomly_generated_choice

        elif user_input == 'N':
         print('Okay, we will try something else!')
         continue

        else: 
         print('Please select Y or N.')
         continue

choosen_transportation = transportation_generator()

def restaurant_generator():
    valid_response = True 

    while valid_response == True:
        randomly_generated_choice = random.choice(restaurants)   
        user_input = input(f'You will be dining at {randomly_generated_choice}. Do you like this choice? Enter Y or N: ')

        if user_input == 'Y':
         print('Yaaaaaaaay! Great choice!')
         return randomly_generated_choice

        elif user_input == 'N':
         print('Okay, we will try something else!')
         continue

        else: 
         print('Please select Y or N.')
         continue

choosen_restaurant = restaurant_generator()

def entertainment_generator():
    valid_response = True

    while valid_response == True:
        randomly_generated_choice = random.choice(entertainment)   
        user_input = input(f'You will be {randomly_generated_choice}. Do you like this choice? Enter Y or N: ')

        if user_input == 'Y':
         print('All choices have been selected! Your day trip is now complete!')
         return randomly_generated_choice

        elif user_input == 'N':
         print('Okay, we will try something else!')
         continue

        else: 
         print('Please select Y or N.')
         continue

choosen_entertainment = entertainment_generator()

def exit_message():

    print("Lets do a recap for your trip!")

exit_message()

print(choosen_destination)
print(choosen_transportation)
print(choosen_restaurant)
print(choosen_entertainment)





 

  



        


      










    
