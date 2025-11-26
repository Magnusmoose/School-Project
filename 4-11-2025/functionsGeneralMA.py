import time

def coolPrint(text):
    for character in text:
        print(character, end = "")
        time.sleep(0.05)
    print(end = "\n")