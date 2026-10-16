from greetings import getusername,build_greeting
from help_menu import print_help
from game import play_guessing_game
from datetime_utils import get_current_time,get_current_date,get_current_hour
from content import get_random_quote,get_random_jokes,get_random_fact
from calculator import parse_exp,calculate
from ai_concepts import recommend_activity,run_perceptron_demo,run_hidden_layer_demo



EXIT_WORDS = ("quit",)

def normalise(text):
    return text.strip().lower()


def handle_command(user_input,name):
    text = normalise(user_input)
    if any(word in text.split() for word in EXIT_WORDS):
        print(f"Assistant : Goodbye, {name}!")
        return False
    elif text in ("help","commands"):
        print_help()
    elif any(greeting in text for greeting in ("hello","hi")):
        print("Hello how are you?")
    elif "time" in text:
        print(f"Assistant: Today's time is {get_current_time()}.")
    elif "date"  in text:
        print(f"Assistant: Today's date is {get_current_date()}.")
    elif "calculate" in text or any(op in text for op in ("+","-","*","/")):
        parsed = parse_exp(text)
        if parsed:
            num1,operator,nums = parsed
            print(f"Assistant: {calculate(num1,operator,nums)}")
        else:
            print("Assistant : I Couldn't understand that")
    elif "quote" in text:
        print(f"Assistant: \"{get_random_quote()}\"")
    elif "joke" in text:
        print(f"Assistant:{get_random_jokes()}")
    elif "fact" in text:
        print(f"Assistant: {get_random_fact()}")
    elif "game" in text or "guess" in text:
        play_guessing_game()
    elif "recommend" in text or "suggest" in text:
        print(recommend_activity())
    elif "perceptron" in text or "neuron" in text:
        first_output = run_perceptron_demo()
        run_hidden_layer_demo(first_output)
    else:
        print(f"Assistant: Sorry {name}, I didnt understand that.Try 'Help'")
    return True




def main():
    try:
        name = getusername()
        print(build_greeting(name))
        running = True
        while running:
            user_input = input(f"\n{name} :  ")
            running = handle_command(user_input,name)
    except KeyboardInterrupt:
        print("\n Assistant: Session Interrupted. Goodbye!")
    except Exception as error:
        print(f"Assistant: Something went wrong({error})")

if __name__ == "__main__":
    main()

