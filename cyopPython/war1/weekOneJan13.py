global firstName
global lastName
global voterAge
global citizenshipStatus
global voterZipcode
global voterState


def thankYouForVoting():

    print("")
    print("Part 7/7")
    print("Thank you for registering to vote. Here is the information we recived:")
    print(f"Full Name: {firstName} {lastName}")
    print(f"Age: {voterAge}")
    print(f"U.S Citizenship status: {citizenshipStatus} ")
    print(f"State: {voterState}")
    print(f"Voter Zipcode: {voterZipcode}")
    print("")
    print("Thanks for trying the Voter Registration Application. Your voter registration card should be shipped witin 3 weeks.")

def exitVoterRegistration():

    print("You have exited the Voter Registration")
    exit()

def getAge():

    print("")
    print("Part 2/7")
    continueWithRegistration()
    print("")
    print("Please enter in your age:")

    global voterAge
    voterAge = input()
    
    try:
        x = int(voterAge)
        if x < 18:
            print("Sorry you are too young to vote.")
            exitVoterRegistration()
        
        if x > 110:
            print(f"Sorry, {voterAge} is not a valid age. Exiting program")
            exitVoterRegistration()

        if x >= 18:
            return None

    except ValueError:
        print("")
        print(f"You entered {voterAge}, which is not a valid age. Would you like to try again?")
        
        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            getAge()
        elif t == "no":
            exitVoterRegistration()
    
def continueWithRegistration():

    wantsToContinue = "yes"
    doesNotWantToContinue = "no"
    voterRegistrationPrompt = "Do you want to continue with Voter Registration?"

    print(voterRegistrationPrompt)
    voterRegistrationPromptAnswer = input()
    x = voterRegistrationPromptAnswer.lower()


    if x == wantsToContinue:
        return None

    elif x == doesNotWantToContinue:
        exitVoterRegistration()
    else:
        print("I'm sorry I didn't understand that. Would you like to try again?")
        tryAgain = input()

        if tryAgain == "yes":
            continueWithRegistration()
        elif tryAgain == "no":
            exitVoterRegistration()
        else:
            continueWithRegistration()

def citizenCheck():

    print("")
    print("Part 1/7")
    continueWithRegistration()

    global citizenshipStatus
    isCitizen = "yes"
    isNotCitizen = "no"

    print("")
    print("Are you a citizen of the United States?")
    
    citizenshipStatus = input()
    x = citizenshipStatus.lower()


    if x == isCitizen:
        return None
    elif x == isNotCitizen:
        print("Only US citizens can vote.")
        exitVoterRegistration()
    else:
        print("I didn't understand that sorry. Would you like to try again?")

        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            citizenCheck()
        elif t == "no":
            exitVoterRegistration()

def getVoterState():

    print("")
    print("Part 5/7")
    continueWithRegistration()

    print("")
    print("Enter the 2 letter initial of the state you currently reside in. If you live in Virginia, enter VA. If you live in New York, enter NY. Etc ")

    global upperVoterState
    global voterState


    voterState = input()

    x = voterState

    if x.isnumeric() == True:
        print(f"Your input is invalid. Would you like to try again?")
        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            getVoterState()
        elif t == "no":
            exitVoterRegistration()

    
    if len(x) == 2:
        return None

    if len(x) > 2:
        print(f"You entered {x}, which is greater than the 2 charecter limit for a state. Would you like to try again?")
        tryAgain = input()
        
        if tryAgain == "yes":
            getVoterState()
        elif tryAgain == "no":
            exitVoterRegistration()
        else:
            print("I didn't understand that. If you'd like to try your state again, enter yes. If you'd like to exit, enter no.")
            getVoterState()

    elif x == "":
        print(f"You entered a blank space, which is not vaild. Would you like to try again?")
        tryAgain = input()
        
        if tryAgain == "yes":
            getVoterState()
        elif tryAgain == "no":
            exitVoterRegistration()
        else:
            print("I didn't understand that. Try again.")
            getVoterState()

def getVoterZipcode():

    print("")
    print("Part 6/7")
    continueWithRegistration()
    print("")
    print("Enter your 5 digit zipcode i.e 20744 | 22309 | 84251.")
        
    global voterZipcode
    voterZipcode = input()

    try:
        int(voterZipcode)
        if len(voterZipcode) == 5:
            return None

        elif len(voterZipcode) != 5:
            print("")
            print("Your zipcode is not 5 numbers long. Would you like to try again?")
            tryAgain = input()
            t = tryAgain.lower()

            if t == "yes":
                getVoterZipcode()
            elif t == "no":
                exitVoterRegistration()

    except ValueError:
        print("")
        print("You did not enter a valid 5 digit zipcode. Would you like to try again?")
        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            getVoterZipcode()
        elif t == "no":
            exitVoterRegistration()

def getFirstName():
        
        print("")
        print("Part 3/7")
        continueWithRegistration()

        print("")
        print("Enter your first name:")

        global firstName
        firstName = input()

        if firstName.isalpha():
            return None
        
        elif firstName.isalpha() == False:
            print("Please make sure your name has no numbers or special charecters. Would you like to try again?")
            tryAgain = input()

            if tryAgain == "yes":      
                getFirstName()
            elif tryAgain == "no":
                exitVoterRegistration()            
            else:
                print("I'm not sure what you mean, restarting questionare.")
                getFirstName()

def getLastName():
        
        print("")
        print("Part 4/7")
        continueWithRegistration()

        print("")
        print("Enter your last name:")

        global lastName
        lastName = input()
        if lastName.isalpha():
            return None
        elif lastName.isalpha() == False:
            print("Please make sure your name has no numbers or special charecters. Would you like to try again?")
            tryAgain = input()

            if tryAgain == "yes":      
                getLastName()
            elif tryAgain == "no":
                exitVoterRegistration()            
            else:
                print("I'm not sure what you mean, restarting questionare.")
                getLastName()



#Intro
print("Welcome to the Python Voter Registration Application.")

#Funcs
continueWithRegistration()
citizenCheck()
getAge()
getFirstName()
getLastName()
getVoterState()
getVoterZipcode()
thankYouForVoting()









