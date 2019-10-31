import pandas as pd
csv = pd.read_csv("df_fighters_clean_final.csv")
csv["Name"] = csv["Name"].str.lower()
csv.to_csv("df_fighters_clean_final.csv", index=False)
