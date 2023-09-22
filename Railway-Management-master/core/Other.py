import os
import time


def About():
    with open(r"C:\Users\unqki\Downloads\Railway-Management-master\Railway-Management-master\README.md") as file:
        data = file.read()
        print(data)

def ClearScreen():
    print("Clearing..")
    time.sleep(2)
    os.system("cls")

def Menu(answer="Yes"):
    if answer in ["Yes", "Y"]:
        print("  WELCOME TO RAILWAY RESERVATION SYSTEM")
        print("1. Book a Ticket")
        print("2. Cancel a Booking")
        print("3. Check Fares")
        print("4. Show my Bookings")
        print("5. Show Available Trains")
        print("6. Clear Screen")
        print("7. Menu")
        print("8. About")
        print("9. Exit")
    else:
        pass