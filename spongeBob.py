import random

while True:
    text = input("Paste the text you want to scramble: ")


    def randomlyTurnCharUpperOrLower(c):
        if random.random() < 0.5:
            return c.upper()
        else:
            return c.lower()

    output = "".join([randomlyTurnCharUpperOrLower(text[0]), randomlyTurnCharUpperOrLower(text[1])])

    for i in range(2, len(text)):
        c = text[i]
        replacement = c
        if c.isalpha():
            replacement = randomlyTurnCharUpperOrLower(c)
            if(output[i-1].isupper() and output[i-2].isupper()):
                replacement = replacement.lower()
            elif(output[i-1].islower() and output[i-2].islower()):
                replacement = replacement.upper()
        output += replacement

    print(output)

        
