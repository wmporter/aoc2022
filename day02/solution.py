# part 1 strategy
scores = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6,
}

# part 2 strategy
strat_scores = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7,
}

score = 0
strat_score = 0
with open('input') as f:
    for line in f:
        result = line.strip().replace(' ', '')
        score += scores[result]
        strat_score += strat_scores[result]
        
# part 1
print(score)

# part 2
print(strat_score)