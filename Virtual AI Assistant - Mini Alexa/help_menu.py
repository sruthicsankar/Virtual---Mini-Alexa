COMMANDS = [("time","Tell you the current time"),
            ("date","Tells you the current date"),
            ("calculate","Does math"),
            ("Quotes","Shares a quote"),
            ("Joke","Tells a joke"),
            ("fact","Share a random fact"),
            ("game","Starts a fun game"),
            ("recommend","Suggests an activity based on the time of day"),
            ("perceptron","Runs a mini NN demo"),
            ("help","shows this list of commands"),
            ("quit","Ends the session")]


def print_help():
    print("Assistant: Here's  everything I can do.")
    for command,description in COMMANDS:
        print(f"- {command:<28}{description}")
        