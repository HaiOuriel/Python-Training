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
while  number[0] <= 0 or number[0] > 100:
    num = int(input('Enter a number between 1 and 100:\n'))
    number.append(num)
    if number[-1] == random_num:
        print("You guessed it! The number was", random_num)
        break
    if len(number) == 2:
        if abs(number[-1] - random_num) > 10:
            print("COLDER")
        else:
            print("WARMER")
    else:
        if abs(number[-1] - random_num) > 10:
            print("COLD")
        else:
            print("WARM")

