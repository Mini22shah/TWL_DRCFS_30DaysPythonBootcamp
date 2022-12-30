# username = input('Enter the username ')
# password = input('Enter the password ')
# mini =",".join((username,password))

# with open("test.txt",'w') as file:
#     file.write(mini)


# print(mini)
# 1. take username and password of 5 people and save them iin file named test_data.txt
# 2.each username and password should be  in new line
# 3. test_data.txt should contain data in csv



for _ in range(5):
    username = input('Enter the username')
    password = input('Enter the password')
    mini =",".join((username,password))
    with open('test_data.txt','a') as file:
        file.write(mini)
        file.write('\n')
        
    




