from math import floor

# TODO: Add testcases
# Takes a score from 1 to 30 and returns a modifier from -5 to +10
def score_2_modifier(score):
    return floor((score-10)/2)