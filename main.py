import random
 

destinations = ['Las Vegas, NV', 'New York, NY', 'Puerto Rico', 'Orlando, FL', 'Los Angeles, CA']

transportation = [' a bus', 'a train', 'a plane', 'a rental car', 'a ship/boat/ferry']

restaurants = ['Brio Italian Grille', 'Dallas BBQ', 'Casita Miramar', 'Kres Chophouse', 'Water Grill Restaurant']


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
         
         input(f'We selected {transportation} as your form of transporation today. Do you like this choice? Enter Y or N: ')
        
        elif user_input == 'N':
         print('Okay, we will try something else!')
         continue
        
        else: 
         print('Please select Y or N.')
         continue
        
         
destination_generator()  

def transportation_generator():
    valid_response = True

    while valid_response == True: 
        randomly_generated_choice = random.choice(transportation)   
        user_input = input(f'You will be taking {randomly_generated_choice} for today"s trip. Do you like this choice? Enter Y or N:') 
        if user_input == 'Y':
         print('Yaaaaaaaay! Great choice!')
         break
        elif user_input == 'N':
         print('Okay, we will try something else!')
         continue
        else: 
         print('Please select Y or N.')
         continue



def restaurant_generator():
    valid_response = True 

    while valid_response == True:
     randomly_generated_choice = random.choice(restaurants)   





      










    
