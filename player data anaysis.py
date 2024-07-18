import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('/content/player_dataset_cleaned_file.csv')

#omar data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Omar's row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if 'Omar' is present in 'Player Name' column
if 'Omar' in df['Player Name'].unique():
    omar_goals = df[df['Player Name'] == 'Omar'][selected_columns].values.flatten()   
    

omar_total_goals = sum(omar_goals)
print(f"Omar Total Goals = {omar_total_goals}")


#Abdullah data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Abdullah row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Abdullah' is present in 'Player Name' column
if 'Abdullah' in df['Player Name'].unique():
    Abdullah_goals = df[df['Player Name'] == 'Abdullah'][selected_columns].values.flatten()   
    

Abdullah_total_goals = sum(Abdullah_goals)
print(f"Abdullah Total Goals = {Abdullah_total_goals}")



#Zayd data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Zayd row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if 'Zayd' is present in 'Player Name' column
if 'Zayd' in df['Player Name'].unique():
    Zayd_goals = df[df['Player Name'] == 'Zayd'][selected_columns].values.flatten()   
    

Zayd_total_goals = sum(Zayd_goals)
print(f"Zayd Total Goals = {Zayd_total_goals}")








#Idris data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Idris's row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if 'Idris' is present in 'Player Name' column
if 'Idris' in df['Player Name'].unique():
    Idris_goals = df[df['Player Name'] == 'Idris'][selected_columns].values.flatten()   
    

Idris_total_goals = sum(Idris_goals)
print(f"Idris Total Goals = {Idris_total_goals}")


#Rayyan data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Rayyan row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Rayyan is present in 'Player Name' column
if 'Rayyan' in df['Player Name'].unique():
    Rayyan_goals = df[df['Player Name'] == 'Rayyan'][selected_columns].values.flatten()   
    

Rayyan_total_goals = sum(Rayyan_goals)
print(f"Rayyan_goTotal Goals = {Rayyan_total_goals}")


#Amir data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Amir row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Amir is present in 'Player Name' column
if 'Amir' in df['Player Name'].unique():
    Amir_goals = df[df['Player Name'] == 'Amir'][selected_columns].values.flatten()   
    

Amir_total_goals = sum(Amir_goals)
print(f"Amir Total Goals = {Amir_total_goals}")



#Youssef data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Amir row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Amir is present in 'Player Name' column
if 'Youssef' in df['Player Name'].unique():
    Youssef_goals = df[df['Player Name'] == 'Youssef'][selected_columns].values.flatten()   
    

Youssef_total_goals = sum(Youssef_goals)
print(f"Youssef Total Goals = {Youssef_total_goals}")


#Tariq data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Tariq row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Tariq is present in 'Player Name' column
if 'Tariq' in df['Player Name'].unique():
    Tariq_goals = df[df['Player Name'] == 'Tariq'][selected_columns].values.flatten()   
    

Tariq_total_goals = sum(Tariq_goals)
print(f"Tariq Total Goals = {Tariq_total_goals}")



#Samir data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Tariq row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Tariq is present in 'Player Name' column
if 'Samir' in df['Player Name'].unique():
    Samir_goals = df[df['Player Name'] == 'Samir'][selected_columns].values.flatten()   
    

Samir_total_goals = sum(Samir_goals)
print(f"Samir Total Goals = {Samir_total_goals}")




#Hamza data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Hamza row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Hamza is present in 'Player Name' column
if 'Hamza' in df['Player Name'].unique():
    Hamza_goals = df[df['Player Name'] == 'Hamza'][selected_columns].values.flatten()   
    

Hamza_total_goals = sum(Hamza_goals)
print(f"Hamza Total Goals = {Hamza_total_goals}")



#Faris data
# Clean up column names
df.columns = df.columns.str.strip()

# Select Faris row and specific columns related to goals
selected_columns = ['Goals in January', 'Goals in February', 'Goals in March', 'Goals in April',
                     'Goals in May', 'Goals in June', 'Goals in July', 'Goals in August', 'Goals in September',
                     'Goals in October', 'Goals in November', 'Goals in December']

# Check if Faris is present in 'Player Name' column
if 'Faris' in df['Player Name'].unique():
    Faris_goals = df[df['Player Name'] == 'Faris'][selected_columns].values.flatten()   
    

Faris_total_goals = sum(Faris_goals)
print(f"Faris Total Goals = {Faris_total_goals}")



