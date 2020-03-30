def guess_the_no():
    print("Guess the number from 1 to 20")
    guess = int(input())
    if guess == n:
        print("Correct answer")
    elif guess > n:
        print("To high")
        guess_the_no()
    else:
        print("To low")
        guess_the_no()

n = 14
guess_the_no()
