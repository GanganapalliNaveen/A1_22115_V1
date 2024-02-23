import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

file.dropna(subset=['Instructions'], inplace=True)


instructions = file['Instructions']

instruction_Lengths = instructions.str.split().apply(len)

instruction_length_mean = instruction_Lengths.mean()
instruction_length_variance = instruction_Lengths.var()

print("instruction length for mean:", instruction_length_mean)
print("instruction length for variance:", instruction_length_variance)

plt.figure(figsize=(10, 6))
plt.hist(instruction_Lengths, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Instruction Lengths')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()