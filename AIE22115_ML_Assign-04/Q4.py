import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\navee\Downloads\archive\Food Images\Food Ingredients and Recipe Dataset with Image Name Mapping.csv")

print(df.columns)

y = df['Instructions']

class_1 = 0  
class_2 = 1  

subset_df = df[(y == class_1) | (y == class_2)]

X_train, X_test, y_train, y_test = train_test_split(
    subset_df['Cleaned_Ingredients'], subset_df[y], test_size=0.3, random_state=42
)

print("set size for training:", len(X_train))
print("set size for testing:", len(X_test))