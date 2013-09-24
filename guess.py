import random

def generate_number():
    number = random.randint(1, 100)
    return number

print "Hello and welcome to the guessing game."
print "What's your name?"
name = raw_input("> ")
print "Hey, %s, what number am I thinking of?" % name

number = generate_number()
#print number
not_won = True

counter = 0

while not_won:

    no_guessed = raw_input("> ")

    if no_guessed.isdigit():
        no_guessed = int(no_guessed)

        if no_guessed < number:
            print "Too low."
        elif no_guessed > number:
            print "Too high."
        else:
            not_won = False
            print "You win! Good for you."
        counter += 1
    else:
        print "Give me an integer!"


if counter <= 5:
    print "You're really good at this!"
else:
    print "It took you %d tries. Sucker!" % counter