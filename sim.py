import numpy as np

def getSurvivors(arr):
    return np.where(arr >= 1)[0]

SIMS = 10000
COUNT = 5000
MAX_ROUNDS = 100
results = np.zeros((SIMS,MAX_ROUNDS), dtype=int)

for sim in range(SIMS):
    lives = np.zeros((COUNT), dtype=int)
    lives[:] = 3
    round_i = 0
    for round_i in range(MAX_ROUNDS):
        survivors = getSurvivors(lives)
        LS = len(survivors)
        lose_count = round(LS*0.49)
        win_count = round(LS//20)

        eventful = np.random.choice(LS, size=lose_count+win_count, replace=False)
        for e in range(len(eventful)):
            i = eventful[e]
            if e < lose_count:
                lives[survivors[i]] -= 1
            else:
                lives[survivors[i]] += 1

        results[sim,round_i] = len(getSurvivors(lives))
        round_i += 1

for round_i in range(MAX_ROUNDS):
    print(f"{np.mean(results[:,round_i]):.3f}")
