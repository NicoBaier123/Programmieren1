secret_number=9
guess_count=0
guess_limit=3
i=0
guess=0
exit=0

while exit==0:
        while i==0 and exit==0:
            while guess_count<guess_limit and exit==0:
                guess=int(input("Guess: "))
                guess_count +=1
                if guess == secret_number:
                    print("You won!")
                    again=str(input("Press s to play again****""Tap anywhere to exit"))
                    if again.lower()=="s":
                        guess_count=0
                        i=0
                    else:
                        exit=1
                        break
                if guess_count == 3:
                    print("Sorry, you failed!")
                    cont = str(input("press s to start again"))
                    if cont.lower() == "s":
                        i = 0
                        guess_count = 0

        if exit==1:
            print("Congrats!")