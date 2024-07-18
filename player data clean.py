# Step 1: Import pandas library
import pandas as pd

# Step 2: Read the CSV file into a DataFrame
file_path = '/content/player-dataset.csv'  # Replace with your CSV file path
try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # or encoding='latin1'
except FileNotFoundError:
    print(f"Error: File not found at path {file_path}")
    # Add appropriate error handling or exit the script

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Save the cleaned DataFrame back to a new CSV file
cleaned_file_path = 'player_dataset_cleaned_file.csv'
df.to_csv(cleaned_file_path, index=False)