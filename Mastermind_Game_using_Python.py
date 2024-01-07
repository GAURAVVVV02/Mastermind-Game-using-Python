import random

num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0

    while n != num:
        ctr += 1
        count = 0

        # Convert n and num to strings for easier digit extraction
        n_str = str(n)
        num_str = str(num)

        # correct[] list stores digits which are correct
        correct = ['X'] * 4

        for i in range(0, 4):
            if n_str[i] == num_str[i]:
                count += 1
                correct[i] = n_str[i]

        print("Not quite the number. But you did get", count, "digit(s) correct!")

        # Print the correct digits (X represents correct)
        for k in correct:
            print(k, end=' ')
        
        print('\n\n')
        n = int(input("Enter your next choice of numbers: "))

        if count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    # Code should not reach here if the guess is correct, remove redundant check
    ctr += 1
    print("You've become a Mastermind!")
    print("It took you only", ctr, "tries.")
