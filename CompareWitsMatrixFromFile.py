import subprocess
import csv
import numpy as np
import os
import re
import json

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
            percentage = match.group(1) if match else '0'
            row.append(percentage)
        else:
            row.append('100')  # Assuming 100% similarity for the same witness
    matrix.append(row)

# Write the matrix to the output CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([''] + witnesses)  # Write header row
    for i, row in enumerate(matrix):
        csvwriter.writerow([witnesses[i]] + row)

print(f"Comparison matrix saved to {output_file}")