import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import codecademylib3_seaborn
import glob

plt = pyplot
files = glob.glob("states*.csv")
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
df = pd.concat(df_list)

print(df.columns)
print(df)

print(df.head())
df["Income"] = df["Income"].str.extract('(\d+\.\d{2})', expand=True)
df[["Men", "Women"]] = df.GenderPop.str.split("M_", expand=True)

df["Women"] = df["Women"].str.extract('(\d+)')
df['Men'] = df['Men'].astype('str').astype('int64')

df['Women'] = df.apply(
    lambda row: row['TotalPop']-row['Men'] if (row['Women']) is not None else row['Women'],
    axis=1
)
print(df.head(30))

df = df.drop_duplicates()
plt.scatter(df["Women"], df["Income"])
plt.show()
df["Hispanic"] = df["Hispanic"].str.extract('(\d+\.\d+)', expand=True)

print(df.dtypes)

df["White"] = df["White"].str.extract('(\d+\.\d+)', expand=True)
df["Black"] = df["Black"].str.extract('(\d+\.\d+)', expand=True)
df["Native"] = df["Native"].str.extract('(\d+\.\d+)', expand=True)
df["Asian"] = df["Asian"].str.extract('(\d+\.\d+)', expand=True)
df["Pacific"] = df["Pacific"].str.extract('(\d+\.\d+)', expand=True)
df['Hispanic'] = df['Hispanic'].astype('str').astype('float')
df['White'] = df['White'].astype('str').astype('float')
df['Black'] = df['Black'].astype('str').astype('float')
df['Native'] = df['Native'].astype('str').astype('float')
df['Asian'] = df['Asian'].astype('str').astype('float')
df['Pacific'] = df['Pacific'].astype('str').astype('float')

df.hist(bins=10)
plt.show()
print(df.duplicated())