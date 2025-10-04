import pandas as pd
import os

def clean_data(input_file, output_file):
    print("Reading data...")
    df = pd.read_csv(input_file)

    print("Cleaning data...")
    # Drop duplicate rows
    df = df.drop_duplicates()

    # Drop rows with missing values
    df = df.dropna()

    print("Saving cleaned data...")
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")


if __name__ == "__main__":
    # file paths based on your folder structure
    input_file = os.path.join("data", "raw", "raw_data.csv")
    output_file = os.path.join("data", "clean", "cleaned_data.csv")

    clean_data(input_file, output_file)
