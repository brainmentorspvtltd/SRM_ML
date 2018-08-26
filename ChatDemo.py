chat = True

while chat:
    userMessage = input("Enter your message : ")

    if userMessage == "hi" or userMessage == "hello":
        print("Hello User")
    elif userMessage == "bye":
        print("Bye user")
        chat = False
    else:
        print("I Don't understand")
