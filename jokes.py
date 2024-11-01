import random

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why can't you give Elsa a balloon? Because she will let it go!",
        "Why was the broom late? It swept in!",
        "What do you call a factory that makes good products? A satisfactory!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What did one wall say to the other wall? I'll meet you at the corner!",
        "Why do seagulls fly over the ocean? Because if they flew over the bay, they’d be bagels!",
        "What do you call an alligator in a vest? An investigator!",
        "Why did the computer go to the doctor? Because it had a virus!"
    ]
    return random.choice(jokes)

def get_compliment():
    compliments = [
        "You're amazing!",
        "You're a true gem!",
        "You light up the room!",
        "You're a breath of fresh air!",
        "You're doing great!",
    ]
    return random.choice(compliments)
