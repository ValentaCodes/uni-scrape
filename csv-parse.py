import csv
def parse_csv(filename):
    """
    Opens a CSV file and prints each row as a dictionary.
    """
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print(f"Permission denied: {filename}")
    except OSError as e:
        print(f"Error opening file {filename}: {e}")
