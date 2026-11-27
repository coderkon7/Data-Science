import webbrowser


# DATA
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "purple", "lime"]

BOT_FAVS = {"Food":"waffles", "Color":"blue", "Animal":"cheetah"}


invalid_input = "Oops! I didn't catch that."


def askexit():
    asking = True
    while asking:    
        exit = input("Would you like to exit this conversation? (yes/no) : ").strip().lower()
        if exit == "yes":
            asking == False
            return True
        elif exit == "no":
            asking = False
            return False
        else:
            print("Oops! I didn't understand that. Please say yes or no.")

name = input("Hello! I am AI Bot. What's your name? : ").strip().lower().capitalize()

chatting = True
while chatting:

    mood = input(f"Nice to meet you, {name}! How are you feeling today? (good, bad, neutral): ").strip().lower()
    if mood == "good":
        print("Glad to hear it!")
        hobbies = input("What are your favorite hobbies?").strip().lower()
        print("Those sound like great hobbies!")
    elif mood == "bad":
        print("So sorry to hear that. Maybe I can cheer you up!")
        if askexit() == False:
            music = input("Would you like to listen to some music? I can open Spotify for you if you like! (yes/no): ").strip().lower()
            if music == "yes":
                webbrowser.open("https://www.spotify.com")
            elif music == "no":
                color = input(f"Got it! What is your favorite color instead? Mine is {BOT_FAVS['Color']} : ").strip().lower()
                if color in COLORS:
                    print(f"{color} is a great color!")
                else:
                    print(f"That is not a color! You tried to trick me, lol")
            else:
                print(invalid_input)
        else:
            chatting = False
            break
                
    elif mood == "neutral":
        print("Got it. You're chill today.")
        animal = input(f"How about we discuss favorite animals? Mine is the {BOT_FAVS["Animal"]}. What's yours? : ")
    else:
        print("Error. Please only type good, bad, or neutral.")

    if askexit() == False:
        food = input(f"Great! How about we talk about favorite foods? Mine is {BOT_FAVS['Food']}. What's yours? : ")
        print(f"{food} is a great choice!\n Well, it is time for me to go now.")
        chatting = False
        break
    else:
        chatting = False
        break

print("It was great chatting with you! Have a great rest of your day!\nBye!")