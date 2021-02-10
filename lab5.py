'''
lab5 if statement
'''

#3.1

alien_color = 'red'

if alien_color == 'yellow':
    print('You just earned 5 points!')
    
#3.2

alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points!')
    
else:
    print('You just earned 10 points!')
    
#3.3

favorite_fruits = ['banana','apple','grapes']

if 'orange' in favorite_fruits:
    print('You really like orange!')
    
if 'grapes' in favorite_fruits:
    print('You really like grapes!')

if 'mango' in favorite_fruits:
    print('You really like mango!')
    
#3.4

age = 67

if age < 10:
    print('You are a kid.')
elif age < 20:
    print('You are a teenager.')
else:
    print('You are an adult.')
    if age >65:
        print('You are an elder.')