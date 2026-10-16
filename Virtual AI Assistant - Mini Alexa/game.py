import random
import time
Min = 1
Max = 9

attempts = 3

def play_guessing_game():
    target = random.randint(Min,Max)
    attemptsleft = attempts

    print(f"Assistant : Lets play a game.\n"
          f"I am thinking of a number between {Min} and {Max}. "
          f"If you guess wrong I will delete your System32 files")
    # if You came to check if i added a os.remove("C:\Windows\System32")  code ... haha got you
    while attemptsleft > 0:
        guess_text = input(f" You have {attemptsleft} tries left. You have {Min}/{Max} chance to get a correct number. And your number is : ").strip()
        try:
            guess = int(guess_text)
        except ValueError:
            print("Assistant: That doesn't look like a whole number. --try again")
            continue
        attemptsleft -= 1
        if guess == target:
            print(f"Assistant: Wow ... you are lucky!!")
            return
        else:
            print(r"deleting C:\Windows\System32 ....")
            time.sleep(4)
            print("Assistant: Haha Kidding")

    print(f"Assistant: Out of tries! The number was {target}.")

    