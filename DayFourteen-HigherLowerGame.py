import random
lists=[["Mubarak Haruna","Jun_Yun","what.a.trevasty",]
            ,[2618,5300000,1938]
              ]
def HigherLower(Accounts):
    if int(len(Accounts[0]))<2:
        print("That's the end of the game")
        return
    else:
        print("Did not run")   
        A=random.randint(0,len(Accounts)-1)
        B=random.randint(0,len(Accounts)-1)
        print(len(Accounts)-1,"Length test")
        while B==A:
            B=random.randint(0,len(Accounts[0])-1)
        print("Welcome to HigherLower Python edition :)")
        print("The rules are simple, you have to guess if the number of instagram followers will be higher or Lower")
        print("The contestants are", Accounts[0][A], "VS", Accounts[0][B])
        choice=str(input("1 or 2: "))
        match choice:
            case "1":
                if Accounts[1][A]>Accounts[1][B]:
                    print("You win! The number of followers of", Accounts[0][A], "is higher")
                    del Accounts[0][B]
                    del Accounts[B][0]
                    HigherLower(Accounts)
                else:
                    print("You lose! The number of followers of", Accounts[0][B], "is higher")
            case "2":
                if Accounts[1][B]>Accounts[1][A]:
                    print("You win! The number of followers of", Accounts[0][B], "is higher")
                    del Accounts[0][B]
                    del Accounts[B][0]
                    HigherLower(Accounts)
                else:
                    print("You lose! The number of followers of", Accounts[0][A], "is higher")


HigherLower(lists)