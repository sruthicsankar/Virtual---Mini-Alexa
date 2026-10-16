import random

QUOTES = ["The best way to predict the future is to create it.",
          "It is humiliating to remain with our hands folded while others write history. It matters little who wins",
          "A good plan violently executed now is better than a perfect plan executed next week",
          "Lead me, follow me, or get out of my way.",
          "Rules are not necessarily sacred, principles are.",
          "When you see a rattlesnake poised to strike, you do not wait until he has struck to crush him.",
          "It's good to trust others, but, not to do so is much better."]

JOKES = ["Why did the WWII soldier bring a pencil to the battlefield? Because he wanted to draw his weapon!",
         "When I was a kid, my dad always told me anyone could become politician. Now that Im an adult, I believe it … and it gives me nightmares!",
         "I told my computer I needed a break, and it said 'no problem, I'll go to sleep.'"]

FACTS = ["The term 'debugging' was coined by Grace Hopper after a moth was found in a relay of the Harvard Mark II computer in 1947. ",
         "As of 2026, the industry is navigating the end of traditional Moore's Law.  While transistor density can no longer double every two years due to physical limits, progress continues through 3D chip stacking and specialized AI accelerators.  A New Moore's Law has emerged in artificial intelligence, where AI agent capabilities are doubling approximately every seven months, far outpacing traditional hardware gains.",
         "Today, 92% of the world's currency exists only digitally on computers.  The field is also dominated by open-source principles at the infrastructure level: of the world's top 500 supercomputers, nearly all run on Linux, with only a tiny fraction using Windows.",
         "In a historic 2026 milestone, a collaboration between the Institute for Advanced Study and DeepMind utilized the AI system LeanMind to prove the Sylvester-Gallai conjecture, marking the first time AI solved a major open problem in theoretical mathematics.  Furthermore, researchers have refined the complexity of matrix multiplication, pushing the exponent $\omega$ down to 2.3719, optimizing one of the most fundamental operations in computing. ",
         "The first AI chatbot, ELIZA, was created in the 1960s and simulated a therapist."]


def get_random_quote():
    return random.choice(QUOTES)

def get_random_jokes():
    return random.choice(JOKES)

def get_random_fact():
    return random.choice(FACTS)
