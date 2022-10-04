#! python3

# Define main program function.
def main():

    # Obtain user input variables.
    print('<<< Wordlist Password Checker >>>\n')
    userPassword = input('Enter a password: ')
    userWordlist = input('Enter a wordlist: ')

    # Define progam logic.
    try:
        def passwordFinder(userPassword, userWordlist):
            for word in wordlist:
                word = word.strip()
                print('Trying: ' + word)
                if word != userPassword:
                    pass
                else:
                    print('\nMatch found: ' + word)
                    exit()

    # Unexpected error handling.
    except:
        print('An error occurred. Close the program and try again.')
        exit()

        
    # Call function using user variables.
    with open(userWordlist, 'r') as wordlist:
        passwordFinder(userPassword, userWordlist)

main()


            
