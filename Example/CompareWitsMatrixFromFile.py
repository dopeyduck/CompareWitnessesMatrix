import subprocess
import csv
import os
import re
import json
import numpy as np

# Ask for the JSON file location
json_file_path = input("Enter the path to the JSON file: ")

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Extract witnesses from the JSON data
witnesses = data.get('witnesses', [])

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
            match = re.search(r'(\d+(\.\d+)?)%', result)
            percentage = float(match.group(1)) if match else 0.0
            row.append(percentage)
        else:
            row.append(100.0)  # Assuming 100% similarity for the same witness
    matrix.append(row)

# Convert matrix to numpy array for easier manipulation
matrix = np.array(matrix)

# Calculate averages
row_averages = np.mean(matrix, axis=1)
column_averages = np.mean(matrix, axis=0)
overall_average = np.mean(matrix)

# Write the matrix to the output CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([''] + witnesses + ['Average'])  # Write header row
    for i, row in enumerate(matrix):
        csvwriter.writerow([witnesses[i]] + list(np.round(row, 2)) + [np.round(row_averages[i], 2)])
    csvwriter.writerow(['Average'] + list(np.round(column_averages, 2)) + [np.round(overall_average, 2)])

print(f"Comparison matrix saved to {output_file}")