import pandas as pd
import numpy as np


file = pd.read_csv(r"C:\Users\navee\Downloads\archive\Food Images\Food Ingredients and Recipe Dataset with Image Name Mapping.csv")

file.dropna(subset=['Title'], inplace=True)

class_A = file[file['Title'].str.contains('Crispy Salt and Pepper Potatoes', na=False)].copy()
class_B = file[file['Title'].str.contains('Turmeric Hot Toddy', na=False)].copy()

def clean_and_tokenize(ingredients):
    ingredients = ingredients.replace("[", "").replace("]", "").replace("'", "")
    ingredients = ingredients.split(",")
    return [ingredient.strip() for ingredient in ingredients]

class_A['Cleaned_Ingredients'] = class_A['Ingredients'].apply(clean_and_tokenize)
class_B['Cleaned_Ingredients'] = class_B['Ingredients'].apply(clean_and_tokenize)

if len(class_A) > 1:
    class_a_cov_matrix = np.cov(class_A['Cleaned_Ingredients'].apply(len), rowvar=False)
    class_A_intraclass_spread = np.trace(class_a_cov_matrix)
else:
    class_A_intraclass_spread = np.nan

if len(class_B) > 1:
    class_B_cov_matrix = np.cov(class_B['Cleaned_Ingredients'].apply(len), rowvar=False)
    class_B_intraclass_spread = np.trace(class_B_cov_matrix)
else:
    class_B_intraclass_spread = np.nan

class_a_mean_vector = np.mean(class_A['Cleaned_Ingredients'].apply(len), axis=0)
class_b_mean_vector = np.mean(class_B['Cleaned_Ingredients'].apply(len), axis=0)
interclass_distance = np.linalg.norm(class_a_mean_vector - class_b_mean_vector)

print("Intraclass spread for Class A:", class_A_intraclass_spread)
print("Intraclass spread for Class B:", class_B_intraclass_spread)
print("Interclass distance from Class A to Class B:", interclass_distance)