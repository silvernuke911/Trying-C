import numpy as np

# Generate 20 random integers between 1 and 6 (inclusive)
dice_rolls = np.random.randint(1, 7, size=17)

# Generate 20 random integers between 0 and 360 (inclusive)
angles = np.random.randint(0, 361, size=17)

# Print results
print("Dice Rolls:", dice_rolls)
print("Angles:", angles)
