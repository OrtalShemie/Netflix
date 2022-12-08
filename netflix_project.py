# -*- coding: utf-8 -*-

from google.colab import files

uploaded = files.upload()

import pandas as pd
df = pd.read_csv('ViewingActivity.csv')
print(type(df))

df.shape

df.head()

df.sample(n=10)

df["Profile Name"].unique()

df["Device Type"].unique()

df.dtypes

df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df['Duration'] = pd.to_timedelta(df['Duration'])
df.dtypes

df.sample(n=10)

df['Profile Name'].value_counts()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
df['Profile Name'].value_counts().plot(kind='bar')
plt.show()

df['Duration'].sum()

df.sort_values('Start Time')

df.loc[df['Profile Name']=='Dean','Duration'].sum()

df.loc[df['Profile Name']=='Guy','Duration'].sum()

df.loc[df['Profile Name']=='August','Duration'].sum()

df.loc[df['Profile Name']=='Dana','Duration'].sum()

df.loc[df['Profile Name']=='Gal','Duration'].sum()

df.loc[df['Profile Name']=='Dean','Duration'].astype('timedelta64[s]').sum()

viewTime = {}
viewTime.update({"Dean": df.loc[df['Profile Name']=='Dean','Duration'].astype('timedelta64[s]').sum()})
viewTime.update({"Guy": df.loc[df['Profile Name']=='Guy','Duration'].astype('timedelta64[s]').sum()})
viewTime.update({"Dana": df.loc[df['Profile Name']=='Dana','Duration'].astype('timedelta64[s]').sum()})
viewTime.update({"Gal": df.loc[df['Profile Name']=='Gal','Duration'].astype('timedelta64[s]').sum()})
viewTime.update({"August": df.loc[df['Profile Name']=='August','Duration'].astype('timedelta64[s]').sum()})
viewTime

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
plt.bar(*zip(*viewTime.items()))
plt.show()

df['Profile Name'].value_counts()

df.loc[df['Profile Name']=='Guy','Duration'].sum()/27921

df.loc[df['Profile Name']=='Dean','Duration'].sum()/14411

df.loc[df['Profile Name']=='Gal','Duration'].sum()/10233

df.loc[df['Profile Name']=='Dana','Duration'].sum()/9501

df.loc[df['Profile Name']=='August','Duration'].sum()/5015

df['Supplemental Video Type'].value_counts()

df=df.loc[df['Supplemental Video Type'].isnull()]

df['Profile Name'].value_counts()

df.loc[df['Profile Name']=='Guy','Duration'].sum()/25221

df.loc[df['Profile Name']=='Dean','Duration'].sum()/13389

df.loc[df['Profile Name']=='Dana','Duration'].sum()/8419

df.loc[df['Profile Name']=='Gal','Duration'].sum()/8281

df.loc[df['Profile Name']=='August','Duration'].sum()/4823

