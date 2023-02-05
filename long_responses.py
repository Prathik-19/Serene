import random

R_GF = "I tried but they are all out of my neural-network!"
R_ADVICE = "Im not there yet buddy. Ask my homie CHATGPT!"


def unknown():
    response = ["Rephrase that please.",
                "...",
                "Nice!",
                "Not sure what to say"][
        random.randrange(4)]
    return response