# def voterRegistrationPromptfunc():
#     print("")
#     print("Do you want to continue with Voter Registration?")

def thankYouForVoting():
    print("Thank you for registering to vote. Here is the information we recived:")

def exitVoterRegistration():
    print("You have exited the Voter Registration")
def grabNames():
    #this print gives spacing 
    print("")
    continueWithRegistration()

    print("Enter your first name:")
    global firstName
    firstName = input()
    
    print("Enter your last name:")
    lastName = input()

    print(f"Hello {firstName} {lastName}")
def getAge():
   
    print("Please enter in your age:")
    voterAge = input()
    x = int(voterAge)

    if x >= 18:
      print(f"You are {x} years old making you elligible to vote")
    elif x < 18:
      print(f"You are {x} years old. You are not elligible to vote")
      exitVoterRegistration()
    elif x == str(x):
        print("Please enter in a numerical value") 
def continueWithRegistration():
    wantsToContinue = "yes"
    doesNotWantToContinue = "no"
    voterRegistrationPrompt = "Do you want to continue with Voter Registration?"

    print(voterRegistrationPrompt)

    voterRegistrationPromptAnswer = input()
    x = voterRegistrationPromptAnswer.lower()


    if x == wantsToContinue:
        print("Moving on")

    elif x == doesNotWantToContinue:
        exitVoterRegistration()
    else:
        print("I'm sorry I didn't understand that. Would you like to try again?")
        tryAgain = input()

        if tryAgain == "yes":
            continueWithRegistration()
        elif tryAgain == "no":
            exitVoterRegistration()
def citizenCheck():

    isCitizen = "yes"
    isNotCitizen = "no"

    print("Are you a citizen of the United States?")
    citizenshipStatus = input()
    x = citizenshipStatus.lower()


    if x == isCitizen:
        print("Moving on, You are a US citizen")
    elif x == isNotCitizen:
        print("Only US citizens can vote, exiting")
        exitVoterRegistration()
    else:
        print("I didn't understand that sorry. Would you like to try again?")

        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            citizenCheck()
        elif t == "no":
            exitVoterRegistration()
#might put state+zip together
def voterState():
    continueWithRegistration()

    print("Enter the full name of the state you live in. i.e Maryland | California | Nebraska. ")
    voterState = input()
    x = voterState.lower()
    y = x.capitalize()

    print(f"Your state is {y}.")
def voterZipcode():
    continueWithRegistration()
    print("What are the first 5 digits of your zipcode. i.e 20744 | 22309 | 84251.")

    voterZipcode = input()

    print(f"Your zipcode is {voterZipcode}.")
def finalFunction():
    continueWithRegistration()

    thankYouForVoting()
    print(f"Full name: {firstName}")


#Intro
print("Welcome to the Python Voter Registration Application.")


continueWithRegistration()

getAge()

grabNames()

citizenCheck()

voterState()

voterZipcode()

finalFunction()








