import numpy as np

# Assuming 'length' and 'string' are provided
length = int(input("Enter the length of the string: "))
string = input("Enter the string: ")

# Initialize numpy arrays for positions
positions = {'M': [], 'E': [], 'T': [], 'U': []}

# Populate positions
for index, char in enumerate(string):
    if char in positions:
        positions[char].append(index)

# Convert lists to numpy arrays for efficient computation
for char in positions:
    positions[char] = np.array(positions[char])

# Efficient computation of 'METU' subsequences
count_METU = 0
for m in positions['M']:
    e_count = np.sum(positions['E'] > m)
    for e in positions['E'][positions['E'] > m]:
        t_count = np.sum(positions['T'] > e)
        for t in positions['T'][positions['T'] > e]:
            u_count = np.sum(positions['U'] > t)
            count_METU += u_count

print(count_METU)
