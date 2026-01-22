"""Function printing python version."""
import sys
def thank_you_for_voting():
    """Function printing python version."""
    print("")
    print("Part 7/7")
    print("Thank you for registering to vote. Here is the information we recived:")
    print(f"Full Name: {firstName} {lastName}")
    print(f"Age: {voterAge}")
    print(f"U.S Citizenship status: {citizenship_status} ")
    print(f"State: {voterState}")
    print(f"Voter Zipcode: {voterZipcode}")
    print("")
    print("Thanks for trying the Voter Registration Application. " \
    "Your voter registration card should be shipped witin 3 weeks.")
def exit_voter_registration():
    """Function printing python version."""
    print("You have exited the Voter Registration")
    sys.exit()
def get_age():
    """Function printing python version."""
    print("")
    print("Part 2/7")
    continue_with_voter_registration()
    print("")
    print("Please enter in your age:")

    global voterAge
    voterAge = input()
    try:
        x = int(voterAge)
        if x < 18:
            print("Sorry you are too young to vote.")
            exit_voter_registration()
        if x > 110:
            print(f"Sorry, {voterAge} is not a valid age. Exiting program")
            exit_voter_registration()

        if x >= 18:
            return None

    except ValueError:
        print("")
        print(f"You entered {voterAge}, which is not a valid age. Would you like to try again?")

        try_again = input()
        t = try_again.lower()

        if t == "yes":
            get_age()
        elif t == "no":
            exit_voter_registration()
def continue_with_voter_registration():
    """Function printing python version."""
    wants_to_continue = "yes"
    does_not_want_to_continue = "no"
    voter_registration_prompt = "Do you want to continue with Voter Registration?"

    print(voter_registration_prompt)
    voter_registration_prompt_answer = input()
    x = voter_registration_prompt_answer.lower()


    if x == wants_to_continue:
        return None

    elif x == does_not_want_to_continue:
        exit_voter_registration()
    else:
        print("I'm sorry I didn't understand that. Would you like to try again?")
        try_again = input()

        if try_again == "yes":
            continue_with_voter_registration()
        elif try_again == "no":
            exit_voter_registration()
        else:
            continue_with_voter_registration()
def citizen_check():
    """Function printing python version."""
    print("")
    print("Part 1/7")
    continue_with_voter_registration()

    global citizenship_status
    is_citizen = "yes"
    is_not_citizen = "no"

    print("")
    print("Are you a citizen of the United States?")

    citizenship_status = input()
    x = citizenship_status.lower()


    if x == is_citizen:
        return None
    elif x == is_not_citizen:
        print("Only US citizens can vote.")
        exit_voter_registration()
    else:
        print("I didn't understand that sorry. Would you like to try again?")

        try_again = input()
        t = try_again.lower()

        if t == "yes":
            citizen_check()
        elif t == "no":
            exit_voter_registration()
def get_voter_state():
    """Function printing python version."""
    print("")
    print("Part 5/7")
    continue_with_voter_registration()

    print("")
    print("Enter the 2 letter initial of the state you currently reside in. " \
    "If you live in Virginia, enter VA. If you live in New York, enter NY. Etc ")

    global voterState


    voterState = input()

    x = voterState

    if x.isnumeric():
        print("Your input is invalid. Would you like to try again?")
        try_again = input()
        t = try_again.lower()

        if t == "yes":
            get_voter_state()
        elif t == "no":
            exit_voter_registration()

    if len(x) == 2:
        return None

    if len(x) > 2:
        print(f"You entered {x}, which is greater than the 2 charecter" \
               "limit for a state. Would you like to try again?")
        try_again = input()

        if try_again == "yes":
            get_voter_state()
        elif try_again == "no":
            exit_voter_registration()
        else:
            print("I didn't understand that. Trying again")
            get_voter_state()

    elif x == "":
        print("You entered a blank space, which is not vaild. Would you like to try again?")
        try_again = input()

        if try_again == "yes":
            get_voter_state()
        elif try_again == "no":
            exit_voter_registration()
        else:
            print("I didn't understand that. Try again.")
            get_voter_state()
def get_voter_zipcode():
    """Function printing python version."""
    print("")
    print("Part 6/7")
    continue_with_voter_registration()
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
            try_again = input()
            t = try_again.lower()

            if t == "yes":
                get_voter_zipcode()
            elif t == "no":
                exit_voter_registration()

    except ValueError:
        print("")
        print("You did not enter a valid 5 digit zipcode. Would you like to try again?")
        try_again = input()
        t = try_again.lower()

        if t == "yes":
            get_voter_zipcode()
        elif t == "no":
            exit_voter_registration()
def get_first_name():
    """Function printing python version."""

    print("")
    print("Part 3/7")
    continue_with_voter_registration()

    print("")
    print("Enter your first name:")
    global firstName

    firstName = input()

    if firstName.isalpha():
        return None

    print("Please make sure your name has no numbers or \
              special charecters. Would you like to try again?")
    try_again = input()

    if try_again == "yes":
        get_first_name()

    elif try_again == "no":
        exit_voter_registration()
    else:
        print("I'm not sure what you mean, restarting questionare.")
    get_first_name()



#Intro
print("Welcome to the Python Voter Registration Application.")

def get_last_name():
    """Function printing python version."""

    print("")
    print("Part 4/7")
    continue_with_voter_registration()

    print("")
    print("Enter your last name:")

    global lastName
    lastName = input()
    if lastName.isalpha():
        return None
    if lastName.isalpha():
        print("Please make sure your name has no numbers or \
                    special charecters. Would you like to try again?")
        try_again = input()

        if try_again == "yes":
            get_last_name()
        elif try_again == "no":
            exit_voter_registration()
        else:
            print("I'm not sure what you mean, restarting questionare.")
            get_last_name()


#Funcs
continue_with_voter_registration()
citizen_check()
get_age()
get_first_name()
get_last_name()
get_voter_state()
get_voter_zipcode()
thank_you_for_voting()
