import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def shift_positions():
    # Builds the game table with the shift positions for the Snakes and Ladders squares
    table = [0 for x in range(36)]
    table[1] = 14
    table[4] = 6
    table[8] = 26
    table[16] = 3
    table[17] = 28
    table[19] = 5
    table[23] = 15
    table[24] = 34
    table[31] = 29
    table[33] = 11
    return table

def markov_chain(shift):
    # Builds the Markov Chain for the table which indicates the probability of reaching a table square from another
    chain = np.zeros(shape=(36,36))
    for x in range(len(chain)):
        for y in range(len(chain[x])):
            # Calculate the probabilities for x+1
            if (x+1) < 36 and y > x:
                if shift[x+1] == 0:
                    chain[x][x+1] = 0.5
                else:
                    chain[x][shift[x+1]] = 0.5
            # Calculate the probabilities for x+2
            if (x+2) < 36 and y > x:
                if shift[x+2] == 0:
                    chain[x][x+2] = 0.5
                else:
                    chain[x][shift[x+2]] = 0.5
    return chain

def power_method(markov, times):
    # Applies the power method in a given Markov chain as many <times> as needed
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

def main():
    S = shift_positions()
    M = markov_chain(S)
    G = nx.from_numpy_matrix(M)

    nx.draw_networkx(G)
    plt.savefig('markov_chain.png')

    P = power_method(M, 100)
    for x in range(36):
        print("Pos #%i = %.5f" %(x+1, P[x]*100))
    
main()
