# status = False
# name = input('Enter any word:')
# for ch in name:
#     if ch.islower():
#         status = True
# print(status)
# if status:
#     print('The word contains lowercase')
# else:
#     print('The word doesnot contain lowercase')
        



# name = input('Enter any word:')
# if name.isupper() == True:
#     print('The word contains uppercase')
# else:
#     print('The word doesnot contain uppercase')


# name = input('Enter any word:')
# if name.isdigit() == True:
#     print('The word contains numbers')
# else:
#     print('The word doesnot contain numbers')    


# import string
# name = input('Enter any word:')
# special_character = string.punctuation
# if special_character == True:
#     print('The word contains special characters')
# else:
#     print('The word doesnot contain special characters')



# 1.pass the user_input in a function
# 2. take the user_input and determine whether it contains lower case or not inside a function and 
# 3. the function should return the bool value i.e. either True or False 
# 4. Taking the status print the message
# a.normally 
# b.list comprehension with any()


# def has_lower(username):
#     status = False
#     for ch in username:
#         if ch.islower() == True:
#             status = True
#     return status
            
       

# username = input('Enter the name:')

# # print(username)
    

# result = has_lower(username)
# print(result)

# import string
# def has_special_character(username):
#     status = False
#     for ch in username:
#         if ch in special_character:
#             status = True
#     return status
            
       

# special_character = list(string.punctuation)
# # print(special_character)
# username = input('Enter the name:')

# result = has_special_character(username)
# print(result)



#------------------------------------------------------------------------------------

# 1.take input from user i.e. password
# 2.make four function i.e.
# --> to check for lowercase
# --> to check for uppercase
# --> to check for special character
# --> to check for digits
# 3. rank password 
# i.e. POOR, MODERATE,STRONG

# 4.conditions
# i. POOR
# number of characters less than 8 and contains below 3 conditions
# ii.MODERATE
# number of characters  in between 8 to 10 and satisfies more than 3 condition
# iii.STRONG
# number of character greater than 10 and satisfy all four condition
# zam-obsh-jyy

#--------------------------------------------------------------------------------------




# password = input('Enter the password:')

# result = has_lower(password)
# print(result)

# result = has_upper(password)
# print(result)

# result = has_number(password)
# print(result)

# result = has_special_character(password)
# print(result)






#test_data.txt--->  username,password
#--> read---> password extract ---> split
#        ----> password rank garera rank return to main function 
#main function -->  username,paswword,   strength--->    csv convert garera file(output.txt)-->write



import string


def has_lower(password):
    status = False
    
    for ch in password:
        
        if ch.islower() == True:
            status = True
    return status


def has_upper(password):
    status = False
    
    for ch in password:
        
        if ch.isupper() == True:
            status = True
    return status


def has_number(password):
    status = False

    for ch in password:
        if ch.isdigit() ==True:
            status = True
    return status 


def has_special_character(password):
    status = False
    special_character =list(string.punctuation)

    for ch in password:
        if ch in special_character:
            status = True
    return status

def rank(password: str):
    if len(password)<8 or (has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password))<3:
        return'POOR'
    

    elif len(password)<=10 and (has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password)) == 3:
        return'MODERATE'
    

    elif len(password)>10 and (has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password)) == 4:
        return'STRONG'


with open('../../Week 2/Assignments/password-10.txt','r') as file:
    content = file.read().split('\n')[:-1]
    print(content)

for ele in content:
    username,password = ele.split(',')
    print('*'*30)
    print(username)
    print(password)


    strength = rank(password)
    print(strength)

    with open('strength.txt','a') as file:
        mini = ','.join((username,password,strength))
        file.write(mini)
        file.write('\n')




    

