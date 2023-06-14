input_file_path = "output.txt"  # Replace with the path to your input file
output_file_path = "table.html"  # Replace with the desired output file path

# Read data from the input file
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()

# Process the data
data = []
for line in lines:
    line = line.strip()
    if line:
        row = line.split()
        rank = row.pop()  # Extract the rank (last element)
        row.insert(0, rank)  # Insert the rank at the beginning
        data.append(row)

# Generate HTML table
html_table = "<table>\n"

# Header row
html_table += "\t<tr>\n"
html_table += "\t\t<th>Rank</th>\n"
html_table += "\t\t<th>Name</th>\n"
html_table += "\t\t<th>School</th>\n"
html_table += "\t\t<th>Score</th>\n"
html_table += "\t</tr>\n"

# Data rows
for row in data:
    html_table += "\t<tr>\n"
    html_table += f"\t\t<td>{row[0]}</td>\n"
    html_table += f"\t\t<td>{' '.join(row[1:-2])}</td>\n"
    html_table += f"\t\t<td>{row[-2]}</td>\n"
    html_table += f"\t\t<td>{row[-1]}</td>\n"
    html_table += "\t</tr>\n"

html_table += "</table>"

# Save HTML table to a file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(html_table)

# Print a success message
print("HTML table saved to:", output_file_path)
