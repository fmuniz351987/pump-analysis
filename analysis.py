#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('out.csv', usecols=['type','difficulty','taps','jumps','hands'])
df = df[df['difficulty'] != 99]

single = df[df['type'] == 'single']
single = single.groupby(by='difficulty').mean()
single.to_csv('single.csv')

single.plot()
plt.grid()
plt.title('Single difficulty charts')
plt.ylabel('Number of steps')
plt.xlabel('Difficulty level')
plt.show()


double = df[df['type'] == 'double']
double = double.groupby(by='difficulty').mean()
double.to_csv('double.csv')

double.plot()
plt.grid()
plt.title('Double difficulty charts')
plt.ylabel('Number of steps')
plt.xlabel('Difficulty level')
plt.show()
