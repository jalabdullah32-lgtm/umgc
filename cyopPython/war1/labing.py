    print("")
    print("Part 4/7")
    continueWithRegistration()
    print("")
    print("Enter your 5 digit zipcode i.e 20744 | 22309 | 84251.")

    voterZipcode = input()

    try:
        x = int(voterZipcode)
    except ValueError:
        print("")
        print("You did not enter a valid 5 digit zipcode. Would you like to try again?")
        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            getVoterZipcode()
        elif t == "no":
            exitVoterRegistration()


    if len(voterZipcode) == 5:
        return None

    elif len(voterZipcode) != 5:
        print("Your zipcode is not 5 numbers long. Would you like to try again?")
        tryAgain = input()
        t = tryAgain.lower()

        if t == "yes":
            getVoterZipcode()
        elif t == "no":
            exitVoterRegistration()
