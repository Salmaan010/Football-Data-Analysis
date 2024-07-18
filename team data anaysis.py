
# Read the CSV file into a pandas DataFrame
df = pd.read_csv("/content/team-dataset.csv")


# access January Total Matches
January_Total_Matches = df.iat[0, 1]
# access February Total Matches
February_Total_Matches = df.iat[1, 1]
# access March Total Matches
March_Total_Matches = df.iat[2, 1]
# access April Total Matches
April_Total_Matches = df.iat[3, 1]
# access May Total Matches
May_Total_Matches = df.iat[4, 1]
# access June Total Matches
June_Total_Matches = df.iat[5, 1]
# access July Total Matches
July_Total_Matches = df.iat[6, 1]
# access August Total Matches
August_Total_Matches = df.iat[7, 1]
# access September  Total Matches
September_Total_Matches = df.iat[8, 1]
# access October  Total Matches
October_Total_Matches = df.iat[9, 1]
# access November Total Matches
November_Total_Matches = df.iat[10, 1]
# access December Total Matches
December_Total_Matches = df.iat[11, 1]



# access January wins
January_wins_match = df.iat[0, 2]
# access February wins
February_wins_match = df.iat[1, 2]
# access March wins
March_wins_match = df.iat[2, 2]
# access April wins
April_wins_match = df.iat[3, 2]
# access May wins
May_wins_match = df.iat[4, 2]
# access June wins
June_wins_match = df.iat[5, 2]
# access July wins
July_wins_match = df.iat[6, 2]
# access August wins
August_wins_match = df.iat[7, 2]
# access September wins
September_wins_match = df.iat[8, 2]
# access October wins
October_wins_match = df.iat[9, 2]
# access November wins
November_wins_match = df.iat[10, 2]
# access December wins
December_wins_match = df.iat[11, 2]






#Percentage find January performance
January_performance  =January_wins_match/January_Total_Matches
print(f"January performance = {January_performance}")


#Percentage find February performance
February_performance  =February_wins_match/February_Total_Matches
print(f"February performance = {February_performance}")

#Percentage find March performance
March_performance  =March_wins_match/March_Total_Matches
print(f"March performance = {March_performance}")

#Percentage find April performance
April_performance  =April_wins_match/April_Total_Matches
print(f"April performance = {April_performance}")

#Percentage find May performance
May_performance  =May_wins_match/May_Total_Matches
print(f"May performance = {May_performance}")

#Percentage find June performance
June_performance  =June_wins_match/June_Total_Matches
print(f"June performance = {June_performance}")

#Percentage find July  performance
July_performance  =July_wins_match/July_Total_Matches
print(f"July performance = {July_performance}")

#Percentage find August performance
August_performance  =August_wins_match/August_Total_Matches
print(f"August_performance = {August_performance}")

#Percentage find September performance
September_performance  =September_wins_match/September_Total_Matches
print(f"September_performance = {September_performance}")

#Percentage find October performance
October_performance  =October_wins_match/October_Total_Matches
print(f"October_performance = {October_performance}")

#Percentage find November performance
November_performance  =November_wins_match/November_Total_Matches
print(f"November_performance = {November_performance}")

#Percentage find December performance
December_performance  =December_wins_match/December_Total_Matches
print(f"December_performance = {December_performance}")

