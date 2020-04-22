import warnings
warnings.filterwarnings('ignore')

import os
#for dirname, _, filenames in os.walk('/kaggle/input'):
#    for filename in filenames:
 #       print(os.path.join(dirname, filename))
        
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#matplotlib inline

# setting plot style for all the plots
plt.style.use('fivethirtyeight')


df = pd.read_csv('top50.csv', encoding="ISO-8859-1")

pd.set_option('display.max_columns', 10)

#Drop the Unnamed: 0 column

df.drop('Unnamed: 0', inplace=True, axis=1)

print(df.head())

# Renaming the columns

df.rename(columns={'Track.Name':'Track Name',
                   'Artist.Name':'Artist Name',
                   'Genre':'Genre',
                   'Beats.Per.Minute':'Beats per Minute',
                   'Energy':'Energy',
                   'Danceability':'Danceability',
                   'Loudness..dB..':'Loudness(dB)',
                   'Liveness':'Liveness',
                   'Valence.':'Valence',
                   'Length.':'Length',
                   'Acousticness..':'Acousticness',
                   'Speechiness.':'Speechiness',
                   'Popularity':'Popularity'}, inplace=True)


print(df.head())

df.info()


print('Number of rows in the dataset: ',df.shape[0])
print('Number of columns in the dataset: ',df.shape[1])

df.describe().round(decimals=3)

plt.figure(figsize=(8,4))
sns.distplot(df['Beats per Minute'], kde=False, bins=18,color='#3ff073', hist_kws=dict(edgecolor="black", linewidth=0.5))
#plt.show()


minimum_beats_per_min = df[df['Beats per Minute'] == df['Beats per Minute'].min()]
minimum_beats_per_min[['Track Name', 'Artist Name', 'Genre', 'Beats per Minute']].reset_index().drop('index', axis=1)

print(minimum_beats_per_min)

maximum_beats_per_min = df[df['Beats per Minute'] == df['Beats per Minute'].max()]
maximum_beats_per_min[['Track Name', 'Artist Name', 'Genre', 'Beats per Minute']].reset_index().drop('index', axis=1)

print(maximum_beats_per_min)


plt.style.use('fivethirtyeight')
plt.figure(figsize=(18,8))
sns.countplot(x='Genre', data = df, linewidth=2, edgecolor='black')
plt.xticks(rotation=90)
plt.show()











