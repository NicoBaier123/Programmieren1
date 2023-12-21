selection=""
started=False
while 1==1:
    selection=input(">").lower()
    if selection == "help":
        print("""
        start-to start the car
        stop-to stop the car
        quit-to quit
        """)
    elif selection.lower()=="start":
        if not started:
            print("Car started...Ready to go!")
        elif started=True:
            print("Car is already started")
    elif selection.lower()==("stop"):
        if started=True:
            print("Car stopped.")
        elif not started:
            print("Car is already stopped")
    elif selection=="quit":
        break
    else:
        print("Sorry, I don't understand that...")