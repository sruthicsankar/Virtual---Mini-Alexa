def getusername():
    name = input("Hello. What is your name?")

    if not name:
        name = ">>>"
    return name

def build_greeting(name):
    return (
        f"Assistant: Nice to Meet you , {name}. I am a Bot and I like to chat ,tell jokes, and to do maths. \n --for more help type 'help' "
        

    )
