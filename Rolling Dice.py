# Hw2dice.py

# Name(s): Khanh Nguyen

#Date: October 8, 2015

import random

n2 = 0 # variable of number dice rolls
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0
n11 = 0
n12 = 0
num_rolls = int(raw_input('Enter number of rolls:\n')) # the number of dice that you want to roll

if num_rolls >= 1:
    while num_rolls >=1: #
        n2 = 0 # it resets the number of dice that I want to change
        n3 = 0 # it resets the number of dice that I want to change
        n4 = 0 # it resets the number of dice that I want to change
        n5 = 0 # it resets the number of dice that I want to change
        n6 = 0 # it resets the number of dice that I want to change
        n7 = 0 # it resets the number of dice that I want to change
        n8 = 0 # it resets the number of dice that I want to change
        n9 = 0 # it resets the number of dice that I want to change
        n10 = 0 # it resets the number of dice that I want to change
        n11 = 0 # it resets the number of dice that I want to change
        n12 = 0 # it resets the number of dice that I want to change
        for i in range(num_rolls): # the number of the dice will roll range from 2 to 12:
            die1 = random.randint(1,6) # random rolls to from # 1 - 6 for first dice
            die2 = random.randint(1,6) # random rolls to from # 1 - 6 for second dice
            roll_total = die1 + die2 # the total number of roll add together w/ die1 and die2

        #Count number of sixes and sevens
            if roll_total == 2: # out of dice roll
                n2 = n2 + 1 # the outcome of the dice roll plus 1
            if roll_total == 3:
                n3 = n3 + 1
            if roll_total == 4:
                n4 = n4 + 1
            if roll_total == 5:
                n5 = n5 + 1
            if roll_total == 6:
                n6 = n6 + 1
            if roll_total == 7:
                n7 = n7 + 1
            if roll_total == 8:
                n8 = n8 + 1
            if roll_total == 9:
                n9 = n9 + 1
            if roll_total == 10:
                n10 = n10 + 1
            if roll_total == 11:
                n11 += 1
            if roll_total == 12:
                n12 += 1
            print 'Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2)

# the outcome of how many times the dice rolls
        print '\nDice roll statistics:'
        print '2s:', n2 # the outcome of how many times the dice rolls
        print '3s:', n3 # the outcome of how many times the dice rolls
        print '4s:', n4 # the outcome of how many times the dice rolls
        print '5s:', n5 # the outcome of how many times the dice rolls
        print '6s:', n6 # the outcome of how many times the dice rolls
        print '7s:', n7 # the outcome of how many times the dice rolls
        print '8s:', n8 # the outcome of how many times the dice rolls
        print '9s:', n9 # the outcome of how many times the dice rolls
        print '10s:', n10 # the outcome of how many times the dice rolls
        print '11s:', n11 # the outcome of how many times the dice rolls
        print '12s:', n12 # the outcome of how many times the dice rolls

# Histogram Dice Charts
        print '\n Histogram Dice Chart:'
        print '2s:', n2 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '3s:', n3 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '4s:', n4 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '5s:', n5 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '6s:', n6 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '7s:', n7 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '8s:', n8 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '9s:', n9 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '10s:', n10 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '11s:', n11 * '*' # total number of dice will multiply "*" based on the number of the outcome
        print '12s:', n12 * '*' # total number of dice will multiply "*" based on the number of the outcome
        num_rolls = int(raw_input('Enter the number of roll again:\n')) # you can put new number of dice that you want to roll

else:
    print 'Invalid number of rolls. Try again.'

