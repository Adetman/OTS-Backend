#Welcome Message
print('WELCOME TO THE LOGIN PROJECT')

#Define Login
def login():
    login_username = 'admin'
    login_password = 'Administrator'

    #User Input
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    #Check if the username and password are correct
    if username == login_username and password == login_password:
        print('Login successful! Welcome,', username)
    else:
        print('Login failed! Please check your username and password.')

#call the login function
login()

