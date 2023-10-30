"""
Game of googol, reference: https://www.semanticscholar.org/paper/On-the-game-of-googol-Hill-Krengel/064b8720acd0e6dfeb7a70bf22e4f29e0d453c9b
see this video from vsauce2 for more info https://www.youtube.com/watch?v=OeJobV4jJG0

Rules:
-max_number is the highest number in the set
-simulations is the number of times you simulate this game and get the resulting output

Note: in the research paper it is mentioned that this strategy should give you a win rate of about 38%, so there must be an error in this script as results differs


Some results:
    
    With 100M as highest possible number, 100 tiles and 50 allowed attempts (37 from eulers), the win rate is about 8%.
    Without the allowed attempts max, this goes up to about 22%.
    Allowing 60% of the grid to be picked, it result in about 12,4%.
    Stopping at 37 result in about 1% win rate.

"""

import random
import math
from tqdm import tqdm

#------------------Simulation variables------------------
max_number = 10000  # The highest number to reach. For perfomance reason, this is not set to a googol
tiles = 100  # The number of "numbers" in the grid
simulations = 100  # Number of game simulations
wins = 0  # Counter for games won
losses = 0  # Counter for games lost

#------------------Simulation variables------------------
print("------------------------------------------------------------------------------")
print(f"Game conditions: \n\t-{max_number} highest possible number\n\t-{tiles} tiles")
print("------------------------------------------------------------------------------\n")

max_in_grid = 0

# Function to generate the initial grid of random numbers and find the highest number
def generate_grid():
    global max_in_grid
    grid = [random.randint(0, max_number) for _ in range(tiles)]
    max_in_grid = max(grid)  # Find the highest number in the grid
    return grid
    

# Loop through the specified number of simulations
for _ in tqdm(range(simulations), desc="Simulations"):
    grid = generate_grid()  # Generate the initial grid and find the highest number
    current_max = 0  # Initialize the current maximum number
    attempts = 0  # Initialize the number of attempts taken
    stop_game = 0 # Check if we got a strong candidate earlier

    # Calculate the number of attempts based on max_number / e
    max_attempts = math.ceil(tiles / 2.71828)  # Approximation of e to 5 decimals

    # Pick tiles based on the euler number strategy (for 100, it's 37 times)
    for i in range(0, max_attempts):
        attempts += 1
        current_max = max(current_max, grid[i])

    # Now pick numbers until a new highest is found, we reach the limit of attempts
    while attempts < tiles:
        attempts += 1
            
        old_max = current_max
        random_index = random.randint(0, tiles - 1)
        new_number = grid[random_index]
        current_max = max(current_max, new_number)
        
        # Close the game only if we found a higher number or we reached the max allowed attempts
        if current_max != old_max:
            break        
        else:
            continue
    else:
        # Here means we didn't found a higher number after max/e attempts, hence we lost the game
        current_max = 0
    
    # Win/Loss counter
    if current_max == max_in_grid:
        wins += 1  # The game was won
    else:
        losses += 1  # The game was lost
    
# Calculate and print the win/loss statistics
win_percentage = (wins / simulations) * 100
loss_percentage = (losses / simulations) * 100

print(f"\nResults on {simulations} simulations:\n")
print(f"Won: {wins} ({win_percentage:.2f}%)")
print(f"Lost: {losses} ({loss_percentage:.2f}%)")


