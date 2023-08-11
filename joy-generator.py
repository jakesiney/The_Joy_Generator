import random

# The Joy Generator

# Complete list of people in the July 23 onsite cohort.
cohort = ["Roberto", "David", "Denise", "Ellie", "Muhammad", "Andrew", "Ami", "Alina", "Emily", "Alex", "Ben", "Senthooran", "Kumani", "Huda", "Carolina", "Zubayda", "Rikie", "Mohsina", "Sarah", "Lateef", "Yasien", "Jake", "Mohsin"]

# A list of the people who have already done the daily joy challenge.
joy_bringers = ["Ben", "Rikie", "Ellie", "Kumani", "Senthooran", "Emily", "Ami", "Denise", "Mohsina", "Sarah", "Jake", "Huda", "Zubayda", "Alex", "Carolina", "Andrew", "Alina", "Roberto", "Denise"]

# A list of people who have not done the daily joy challenge yet.
to_bring_the_joy = [person for person in cohort if person not in joy_bringers]

# Choosing the next person using .random
the_chosen_one = random.choice(to_bring_the_joy)

#  Finally, print the randomly chosen person.
print(the_chosen_one + " is going to bring the joy next!")