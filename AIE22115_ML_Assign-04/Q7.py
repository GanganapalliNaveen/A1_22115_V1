import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv(r"C:\Users\navee\Downloads\archive\Food Images\Food Ingredients and Recipe Dataset with Image Name Mapping.csv")

y_column_name = 'Instructions'  
X = df['Cleaned_Ingredients']
y = df[y_column_name]

df.dropna(subset=['Cleaned_Ingredients', 'Instructions'], inplace=True)

vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(df['Cleaned_Ingredients'])

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, df['Instructions'], test_size=0.3, random_state=42
)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

test_vector_index = 0  
test_vector = X_test[test_vector_index]

test_vector_dense = test_vector.toarray().reshape(1, -1)

predicted_class = neigh.predict(test_vector_dense)
print("Predicted class for the test vector:", predicted_class)