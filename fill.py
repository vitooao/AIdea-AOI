import csv

filename = "labels.csv"
data = {}

# Read the CSV file and convert it to a dictionary
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data[row[0]] = int(row[1])

# Fill in missing values with zeros
for i in range(10142):
    filename = f"test_{i:05d}.png"
    if filename not in data:
        data[filename] = 0

# Write the updated dictionary to a new CSV file
with open("test.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    for filename, label in data.items():
        csvwriter.writerow([filename, label])