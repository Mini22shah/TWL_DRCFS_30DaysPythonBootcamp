import random
random_number = random.randint(1,10)

player_name = input('Enter the name:')
print(f'Player_name:{player_name}')


attempts = 0

while attempts<5:
    guess =int(input('Enter the number:'))
    if guess > random_number:
        print('*'*60)
        print('Your guess is high')
        print('*'*60)   
    elif guess < random_number:
        print('*'*60)
        print('Your guess is low')
        print('*'*60)
    elif guess == random_number:
        print('*'*60)
        print(f'Your guess is correct in {attempts+1} attempts')
        print('*'*60)
        break
    attempts+=1

if guess != random_number:    
        print('*'*60)
        print(f'The correct guess is {random_number}')
        print('*'*60)
    


    




