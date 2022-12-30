for i in range(5):
    name = input('Enter the name :')
    roll_no = int(input('Enter the roll no. :'))
    address = input('Enter the address :')

    with open('data.txt','a') as file:
        mini =','.join((name,str(roll_no),address))
        file.write(mini)
        file.write('\n')

with open('data.txt','r') as file:
    content = file.read().split('\n')[:-1]
    print(content)
flag = 0

username = input('Enter the name:')
for ele in content:
    name,roll_no,address = ele.split(',')
    
    if username == name:
        print(f'{name},{roll_no},{address}')
        flag = 1
if flag == 0:
    print('Name not found')