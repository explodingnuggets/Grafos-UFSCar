```python
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
```
