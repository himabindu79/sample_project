import pandas as pd

def clean_data(input_file, output_file):
    print("Reading data...")
    df = pd.read_csv(input_file)

    print("Cleaning data...")
    # Drop duplicate rows
    df = df.drop_duplicates()

    # Drop rows with any missing values
    df = df.dropna()

    print("Saving cleaned data...")
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")


if __name__ == "__main__":
    # Example usage
    input_file = "data/raw_data.csv"
    output_file = "data/cleaned_data.csv"
    clean_data(input_file, output_file)
