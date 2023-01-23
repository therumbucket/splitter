import csv
import sys

def split_csv(filepath, parts):
    # Open the CSV file
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        # Get the column names from the first row
        headers = next(reader)

        # Get the total number of rows in the file
        row_count = sum(1 for row in reader)

    # Calculate the number of rows per part
    rows_per_part = row_count / parts

    # Open the CSV file again
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        # Get the column names from the first row
        headers = next(reader)

        # Initialize the current row index
        current_row = 0

        # Iterate over the parts
        for i in range(parts):
            # Open a new file for the current part
            with open(f'part-{i}.csv', 'w') as part_file:
                part_writer = csv.writer(part_file)
                # Write the column names to the new file
                part_writer.writerow(headers)

                # Write the rows for the current part
                for row in reader:
                    if current_row > rows_per_part:
                        break
                    part_writer.writerow(row)
                    current_row += 1

if __name__ == '__main__':
    filepath = sys.argv[1]
    parts = int(sys.argv[2])
    split_csv(filepath, parts)
