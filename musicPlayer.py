import winsound
import sys

musicOne = "River_Solo.wav"
musicTwo = "Outlaws_From_The_West.wav"
print("Welcome to Daniel's music player.")

done = False

while not done:
    while True:
        userChoice = input("-\nPress 'P' to play music, 'Q' to quit, 'H' for help : ").upper()

        if userChoice == 'P':
            while True:
                print("-\nMusic Options : 1 = " + musicOne + ", 2 = " + musicTwo + ", Q = Quit")
                option = input("Please enter your choice : ")
                if option == '1':
                    winsound.PlaySound("River_Solo.wav", winsound.SND_FILENAME)
                    continue

                elif option == '2':
                    winsound.PlaySound("Outlaws_From_The_West.wav", winsound.SND_FILENAME)
                    continue


                elif option.upper() == 'Q':
                    break
                else:
                    print("Please enter a valid option")
                    continue
        elif userChoice == 'Q':
            sys.exit()
        elif userChoice == 'H':
            print("-\nIn order to play music, put the music file into the same directory,"
                  "\nIf you want to add your own music, just replace a few lines of code")
            continue
        else:
            print("-\nPlease enter a valid option")
            continue
