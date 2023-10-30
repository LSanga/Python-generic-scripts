"""
Game of googol, reference: https://www.semanticscholar.org/paper/On-the-game-of-googol-Hill-Krengel/064b8720acd0e6dfeb7a70bf22e4f29e0d453c9b
see this video from vsauce2 for more info https://www.youtube.com/watch?v=OeJobV4jJG0

Rules:
-max_number is the highest number in the set
-simulations is the number of times you simulate this game and get the resulting output
(optional added rule)
-attempts_limit is the maximum number of picks you are allowed to take before lock a decision. Default is no more than 50% of the total

Note: in the research paper it is mentioned that this strategy should give you a win rate of about 38%, so there must be an error in this script as results differs


Some results:
    
    With 100M as highest possible number, 100 tiles and 50 allowed attempts (37 from eulers), the win rate is about 8%.
    Without the allowed attempts max, this goes up to about 22%.
    Allowing 60% of the grid to be picked, it result in about 12,4%.
    Stopping at 37 result in about 1% win rate.
    
    If we add a smart version that checks if a number we found earlier is X% close to the maximum allowed, it change the results. 
    In the first case above, if we set the treshold to 10%, win rate in the first case increase to about 10,8%.
    With 5%, it jump to about 19.6% and with 1% goes to about 25%.
    At 1% without limit of attempts, the win rate is about 37,5%.
    
The first approach work blindly: the highest possible number in the grid (max_number) doesn't matter for this strategy to work.
The second consider the max allowed value for numbers and attempt to be smarter.

"""

import random
import math
from tqdm import tqdm

#------------------Simulation variables------------------
max_number = 1000  # The highest number to reach. For perfomance reason, this is not set to a googol
tiles = 100  # The number of "numbers" in the grid
attempts_limit = 100
#attempts_limit = int(tiles * 0.50) # Max number of allowed attemps is X% of the grid, eg. 50%. Defaukt disabled
simulations = 30000  # Number of game simulations
wins = 0  # Counter for games won
losses = 0  # Counter for games lost

# Make the script smarter. Default disabled
threshold_percentage = 0.01  # Threshoold for the distance below
allowed_distance = int(max_number * threshold_percentage) # Calculate the distance to understand if we picked a strong candidate number
#------------------Simulation variables------------------
print("------------------------------------------------------------------------------")
print(f"Game conditions: \n\t-{max_number} highest possible number\n\t-{tiles} tiles\n\t-{attempts_limit} allowed attempts")
#print(f"\t-Stop if we find a number close to the maximum allowed up to {threshold_percentage*100}%")
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

    # Pick tiles based on the euler number, or if we got a number very close to the maximum allowed (if permitted)
    while attempts < max_attempts:
    
        attempts += 1
        # Create a set to keep track of selected indices
        selected_indices = set()

        while True:
            random_index = random.randint(0, tiles - 1)
            # Check if the index has already been selected
            if random_index not in selected_indices:
                selected_indices.add(random_index)   
                current_max = max(current_max, grid[random_index])
                
                """
                # Check if the number is close to the maximum allowed, and exit
                if (abs(max_number - current_max) <= allowed_distance):
                    stop_game = 1
                    attempts = attempts_limit
                    #print (f"Max in grid: {max_in_grid}. Candidate: {current_max}")
                    break
                """
                    
                break
                
    # Now pick numbers until a new highest is found, we reach the limit of attempts or we got a good candidate previously
    while True:
        attempts += 1
        
        # Check early strong candidates
        if stop_game == 1:
            break
            
        old_max = current_max
        random_index = random.randint(0, tiles - 1)
        new_number = grid[random_index]
        current_max = max(current_max, new_number)
        
        # Close the game only if we found a higher number or we reached the max allowed attempts
        if (current_max != old_max) or (attempts >= attempts_limit):
            current_max = new_number
            break        
        else:
            continue
    
    # Win/Loss counter
    if current_max == max_in_grid:
        wins += 1  # The game was won
        #print (f"Won with {attempts}/{attempts_limit} attempts")
    else:
        losses += 1  # The game was lost
    
# Calculate and print the win/loss statistics
win_percentage = (wins / simulations) * 100
loss_percentage = (losses / simulations) * 100

print(f"\nResults on {simulations} simulations:\n")
print(f"Won: {wins} ({win_percentage:.2f}%)")
print(f"Lost: {losses} ({loss_percentage:.2f}%)")


