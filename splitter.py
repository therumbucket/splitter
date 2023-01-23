import csv
import sys
import os

def split_csv(filepath, parts):
    # Open the CSV file
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        # Get the column names from the first row
        headers = next(reader)

        # Get the total number of rows in the file
        row_count = sum(1 for row in reader)

    # Calculate the number of rows per part
    rows_per_part = row_count // parts
    remainder_rows = row_count % parts

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
            filename = os.path.join(os.path.dirname(filepath), f'part-{str(i + 1).zfill(4)}.csv')
            with open(filename, 'w') as part_file:
                part_writer = csv.writer(part_file)
                # Write the column names to the new file
                part_writer.writerow(headers)
                current_row += 1
                # Write the rows for the current part
                for j in range(rows_per_part):
                    if current_row > row_count:
                        break
                    part_writer.writerow(next(reader))
                    current_row += 1
                if remainder_rows > 0:
                    part_writer.writerow(next(reader))
                    current_row += 1
                    remainder_rows -= 1
                print(f'Processing part {i+1}')
    print('Splitting complete!')
    print(f'The parts reside in the directory: {os.path.dirname(filepath)}')
if __name__ == '__main__':
    filepath = sys.argv[1]
    parts = int(sys.argv[2])
    split_csv(filepath, parts)
