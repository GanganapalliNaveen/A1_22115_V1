# NAME  : G.NAVEEN
# REGNO : AIE22115

## Code Explanation

QUESTION 1

In this question, it reads the Excel file containing the purchase date. It extracts relevant columns ('Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)') as matrix A and 'Payment (Rs)' as vector C and prints matrices A and C. It finds the dimensionality of the vector space and, the number of vectors in the vector space by using this it calculates the rank of the matrix of A and finally computes the pseudo-inverse of a matrix of A. Using the pseudo-inverse to calculate the cost of each product based on the given payment vector.

QUESTION 2 

In this question, it reads the Excel file containing the purchase date. It extracts relevant columns ('Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)') as matrix A and 'Payment (Rs) as vector C and prints matrices A and C.it finds the pseudo-inverse of matrix A using Numpy and multiplies this pseudo-inverse of matrix A with the vector C to obtain the model vector X for predicting the cost of products and finally it displays the model vector.

QUESTION 3

In this question, it reads the Excel file containing the purchase data. Adds a new column 'Customer' based on the 'Payment (Rs)' column, labeling customers as 'RICH' if their payment is greater than 200, and 'POOR' otherwise. Defines features X as columns 'Candies (#)', 'Mangoes (Kg)', and 'Milk Packets (#)' and the target variables Y as the customer column. Splitting of the dataset is done into training and testing sets where in my code 70% of the data is used for training and 30% for testing. Creates a K-Nearest Neighbors (KNN) classifier with 5 neighbors using KNeighborsClassifier from scikit-learn. finally makes predictions on the testing dataset using the trained classifier and prints the classification report providing metrics such as precision, recall, and F1-score for each class.


QUESTION 4

In this question, The code analyzes IRCTC stock price data by conducting statistical analysis, calculating probabilities of profit and loss, and visualizing the distribution of percentage changes ('Chg%') by the day of the week, utilizing data import, preprocessing, and visualization techniques to gain insights into stock performance.
