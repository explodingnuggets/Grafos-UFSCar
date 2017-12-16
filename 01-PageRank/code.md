```python
def markov_chain(shift):
    # Builds the Markov Chain for the table which indicates the probability of reaching a table square from another
    chain = np.zeros(shape=(36,36))
    for x in range(len(chain)):
        for y in range(len(chain[x])):
            if (x+1) < 36 and y > x:
                if shift[x+1] == 0:
                    chain[x][x+1] = 0.5
                else:
                    chain[x][shift[x+1]] = 0.5
            if (x+2) < 36 and y > x:
                if shift[x+2] == 0:
                    chain[x][x+2] = 0.5
                else:
                    chain[x][shift[x+2]] = 0.5
    return chain

def power_method(markov, times):
    A = [0 for y in range(36)]
    A[0] = 1

    for n in range(times):
        pos = []
        for i in range(36):
            pos.append(0)
            for j in range(36):
                pos[i] += A[j]*markov[j][i]
        A = pos
    return A
```
