#! python3

import requests

URL = "http://172.20.10.14/phpmyadmin/"
ERROR = 'Access denied'

# Obtain initial login details from user
print("\nSubmit a POST login request to Pi Apache II webserver!")
user = input('\nEnter a username: ')
password = input('Enter a password: ')
print("Submitting POST request...\n")

# sendPOST will submit a POST request to Pi using username and password provided by user.
def sendPOST(user, password):
	data = {"pma_username": user, "pma_password": password, "login": "submit"}
	request = requests.post(URL, data=data)
	if ERROR in request.text:
		print("Error - incorrect login details!")
	else:
		print("Successful login!")
		print(request.text)

# Run the program again.
def runAgain():
	print("\nSubmit a POST login request to Pi Apache II webserver!")
	user = input('\nEnter a username: ')
	password = input('Enter a password: ')
	print("Submitting POST request...\n")
	sendPOST(user, password)
	print("\nRun again? Enter Y or N")
	choice = input(': ')
	if choice == 'Y' or 'y':
		runAgain()
	else:
		exit()

# Call sendPOST function
sendPOST(user, password)

# Initial run again.
print('\nRun again? Enter Y or N')
choice = input(': ')
if choice == 'Y' or 'y':
	runAgain()
else:
	exit()
      
