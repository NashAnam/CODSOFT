import random
import time
import re
from datetime import datetime

def chatbot_response(user_input):
    text = user_input.lower()

    if any(greet in text for greet in ["hello", "hi", "hey", "yo"]):
        replies = [
            "Hey there! How’s it going?",
            "Hello! Hope you're doing good.",
            "Hi! Nice to see you again.",
            "Hey! How’s your day so far?"
        ]
        return random.choice(replies)

    elif "how are you" in text:
        return "I’m just a bot, but I’m feeling talkative today."

    elif "your name" in text:
        return "I’m Buddy — your simple chatbot."

    elif "my name is" in text:
        name = text.split("my name is")[-1].strip().capitalize()
        if name:
            return f"Hi {name}, nice to meet you."
        else:
            return "Nice to meet you."

    elif "thank" in text:
        return "You’re welcome."

    elif "joke" in text:
        tell_joke()
        return None

    elif "time" in text:
        now = datetime.now().strftime("%I:%M %p")
        return f"It’s {now} right now."

    elif "sad" in text:
        return "Don’t be sad. Want to talk about it?"
    elif "happy" in text:
        return "That’s good to hear. Keep it up."
    elif "angry" in text:
        return "Take a deep breath. It helps."
    elif "bored" in text:
        return "Let’s fix that. I can tell you a joke."
    elif "tired" in text:
        return "You should rest a bit."
    elif "stressed" in text or "anxious" in text:
        return "Try to relax. Deep breaths really help."

    math_pattern = re.match(r'^[\d\s\+\-\*/\(\)]+$', text)
    if math_pattern:
        try:
            result = eval(text)
            return f"The answer is {result}"
        except:
            return "That doesn’t look right."

    elif any(word in text for word in ["bye", "exit", "quit"]):
        print("Buddy: Goodbye! Take care.")
        exit()

    elif "who made you" in text:
        return "I was created by a student who is learning AI."

    elif "what can you do" in text:
        return "I can chat, tell jokes, show time, cheer you up, and solve simple math."

    else:
        return "I didn’t quite get that. Try saying it another way."


def tell_joke():
    jokes = [
        ("Why don't scientists trust atoms?", "Because they make up everything!"),
        ("What do you call fake spaghetti?", "An impasta!"),
        ("Why did the math book look sad?", "Because it had too many problems!"),
        ("Why was the computer cold?", "Because it left its Windows open!"),
        ("What do you call cheese that isn’t yours?", "Nacho cheese!")
    ]
    setup, punchline = random.choice(jokes)
    print("Hmm, let me think of a good one...")
    time.sleep(2)
    print(setup)
    time.sleep(2)
    input("(You): ")
    print(punchline)

print("Welcome!.")
print("You can chat, ask me to tell jokes, talk about your mood, check time, or give me math to solve.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    if response:
        print("Buddy:", response)
