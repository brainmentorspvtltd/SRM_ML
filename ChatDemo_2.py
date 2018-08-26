import webbrowser
from datetime import datetime

helloIntent = ["hello","hi","hey","hey buddy","hie"]
byeIntent = ["bye","ok bye"]

chat = True

while chat:
    userMessage = input("Enter your message : ")

    if userMessage in helloIntent:
        print("Hello User")
    elif userMessage in byeIntent:
        print("Bye user")
        chat = False
    elif userMessage.startswith("open"):
        toOpen = userMessage.split()[1]
        webbrowser.open(toOpen+".com")
    elif userMessage == "time":
        t = datetime.now().time()
        print("Time is",t)
    else:
        print("I Don't understand")
