import random, sys
nummin = 1
nummax = 20
num_guesses = 10
num = random.randint(nummin, nummax)
name = input("Hello. What is your name? ")
print("Well, " + name + ", I am thinking of a number between " + str(nummin) + " and " + str(nummax) + ".")
for i in range(1, num_guesses+1):
    guess = input("Take a guess: ")
    try:
        guess_num = int(guess)
    except:
        print("nem számot ütöttél be !")
        continue
    if guess_num == num:
        print("eltaláltad " + str(i) + " lépésben")
        sys.exit()
    else:
        continue
print("csúfos kudarc, " + str(num_guesses) + " lépésben se tudtad kitalálni.")