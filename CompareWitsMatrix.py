import subprocess
import csv
import numpy as np
import os
import re

# Ask for witnesses
witnesses_input = input("Enter the witnesses to be compared (space or comma delimited): ")
witnesses = [w.strip() for w in witnesses_input.replace(',', ' ').split()]

# Ask for database location
database = input("Enter the location of the database: ")

command = './compare_witnesses'
output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output.csv')

# Prepare the matrix
matrix = []

# Compare witnesses and write results to matrix
for item1 in witnesses:
    row = []
    for item2 in witnesses:
        if item1 != item2:
            result = subprocess.run([command, '-f', 'csv', database, item1, item2], capture_output=True, text=True).stdout.strip()
            # Extract the percentage value from the result
            match = re.search(r'\((.*?)%\)', result)
            if match:
                percentage = round(float(match.group(1)), 2)
                row.append(percentage)
            else:
                row.append(np.nan)
        else:
            row.append(np.nan)
    matrix.append(row)

# Convert to numpy array for easier calculations
matrix = np.array(matrix)

# Calculate averages
row_averages = np.round(np.nanmean(matrix, axis=1), 2)
col_averages = np.round(np.nanmean(matrix, axis=0), 2)

# Append averages to matrix
matrix = np.vstack([matrix, col_averages])
matrix = np.hstack([matrix, np.append(row_averages, np.nanmean(row_averages))[:, None]])

# Write matrix to CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([''] + witnesses + ['Average'])
    for item1, row in zip(witnesses, matrix):
        writer.writerow([item1] + list(np.round(row, 2)))
    writer.writerow(['Average'] + list(np.round(matrix[-1], 2)))