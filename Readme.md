# Otree Apps Wide Column Splitter

This Python script takes a CSV file with column names containing a prefix separated by a period (e.g., `participant.id`), and splits the columns into separate CSV files based on the prefix.

## Requirements

- Python 3.6 or higher

## Installation

No additional libraries are required to run this script.

## Usage

1. Save the script as `split_csv.py`.

2. Run the script from the command line, providing the input CSV file path and the output directory path:

```bash
python split_csv.py /path/to/input_file.csv /path/to/output_directory
```
This script will create separate CSV files for each sheet in the specified output directory. The output files will have the same name as the sheet name (e.g., `participant.csv`).

## Example
Given the following input CSV file:
```csv
participant.id,participant.name,session.id,session.date
1,John Doe,101,2023-01-01
2,Jane Smith,102,2023-01-02
```

The script will create two separate CSV files in the output directory:

- `participant.csv`
```csv
id,name
1,John Doe
2,Jane Smith
```
- `session.csv`
```csv
id,date
101,2023-01-01
102,2023-01-02
```

