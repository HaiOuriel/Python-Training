import random
random_num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

number = [0]
while True:
    num = int(input('Enter a number between 1 and 100:\n'))
    if num < 1 or num > 100:
        print("Please enter a number between 1 and 100.")
        continue
    if num == random_num:
        print("You guessed it! The number was", random_num)
        print("You find it in", len(number), "tries.")
        break
    number.append(num)
    if number[-2]:
        if abs(number[-2] - random_num) > abs(number[-1] - random_num): 
            print("COLDER")
        else:
            print("WARMER")

    else:
        if abs(number[-1] - random_num) > 10:
            print("COLD")
        else:
            print("WARM")

