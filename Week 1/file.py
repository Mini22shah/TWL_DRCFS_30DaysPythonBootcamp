import random
import string

def lower_case():    
    value = string.ascii_lowercase
    return value
    

def upper_case(): 
    value = string.ascii_uppercase
    return value

def numbers(): 
    value = '0123456789'
    return value

def special_characters(): 
    value = '!@$%^&*()_+'
    return value

status = True
while status:
    username = input('Enter the username:')
    if len(username) < 20:
        print(username)
        break
    else:
        print('Username must not contain more than 20 characters')




random_password = lower_case()+upper_case()+numbers()+special_characters()
pass_length = 10

password = ''.join(random.sample(random_password,pass_length))
# password = random.sample(random_password,pass_length) -->['*', 'x', '5', '6', 'b', 'B', 'T', '4', 'V', 'L']
print(password)



ask_user = input('Do you want to save the password?(Y/N):')
if ask_user.upper() == 'Y':
    with open('details.txt','a') as file:
        mini=','.join((username,password))
        file.write(mini)
        file.write('\n')

else:
        random_password = lower_case()+upper_case()+numbers()+special_characters()
        pass_length = 10

        password = ''.join(random.sample(random_password,pass_length))
        # password = random.sample(random_password,pass_length) -->['*', 'x', '5', '6', 'b', 'B', 'T', '4', 'V', 'L']
        print(password)

        ask_user = input('Do you want to save the password?(Y/N):')
        if ask_user.upper() == 'Y':
            with open('details.txt','a') as file:
                mini=','.join((username,password))
                file.write(mini)
                file.write('\n')
        else:
            print('Fuck off bro....Get lost!!')








    










