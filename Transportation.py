import random

transportation = [' a bus', 'a train', 'a plane', 'a rental car', 'a ship/boat/ferry']

def welcome_message():
    print("Next we will verify your choice of transportation")


welcome_message()


def transportation_generator():
    user_validator = True
    while user_validator is True:
        randomly_generated_choice = random.choice(transportation)
        user_input_result = input(f'We have choosen {randomly_generated_choice} as your form of transportation')

