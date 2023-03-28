import os
import sys
import argparse
import pandas as pd

def split_csv(input_file, output_directory):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Create a dictionary to store DataFrames for each new sheet
    sheets = {}

    # Iterate through the columns and split them into sheets and column names
    for column in df.columns:
        sheet_name, column_name = column.split('.', 1)

        if sheet_name not in sheets:
            sheets[sheet_name] = pd.DataFrame()

        sheets[sheet_name][column_name] = df[column]

    # Write the resulting DataFrames to separate CSV files
    for sheet_name, sheet_df in sheets.items():
        output_file = os.path.join(output_directory, f'{sheet_name}.csv')
        sheet_df.to_csv(output_file, index=False)

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Split CSV columns into separate files.')
    parser.add_argument('input_file', help='Path to the input CSV file.')
    parser.add_argument('output_directory', help='Path to the output directory.')

    args = parser.parse_args()

    # Create the output directory if it does not exist
    os.makedirs(args.output_directory, exist_ok=True)

    split_csv(args.input_file, args.output_directory)

if __name__ == '__main__':
    main()

