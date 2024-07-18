import pandas as pd

# Load the CSV file into a Pandas DataFrame
file_path = '/content/team-dataset.csv'
df = pd.read_csv(file_path)

# Remove duplicate rows
df = df.drop_duplicates()



# Save the cleaned DataFrame back to a new CSV file
cleaned_file_path = 'team_dataset_cleaned_file.csv'
df.to_csv(cleaned_file_path, index=False)




