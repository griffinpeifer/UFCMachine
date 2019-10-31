import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
df_fighters = pd.read_csv("df_fighters_clean_final.csv")
df_fighters.set_index("Name", inplace=True)
df_matches = pd.read_csv("training_model_clean.csv")


def predict(model, Red, Blue):
    X, y = df_matches.iloc[:, 1:], df_matches.iloc[:, 0]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    stats = ['Height:', 'Weight:', 'Reach:', 'Age', 'SLpM:', 'Str. Acc.:',
             'SApM:', 'Str. Def:', 'TD Avg.:', 'TD Acc.:', 'TD Def.:', 'Sub. Avg.:', 'Win Percentage', 'Total Fights']

    data1 = df_fighters.loc[Red.lower(), stats]
    data2 = df_fighters.loc[Blue.lower(), stats]
    data_diff = (data1 - data2).values.reshape(1, -1)
    data_diff_scaled = scaler.transform(data_diff)
    return loaded_model.predict(data_diff_scaled)


tale_df = pd.read_csv("tale_df.csv")
