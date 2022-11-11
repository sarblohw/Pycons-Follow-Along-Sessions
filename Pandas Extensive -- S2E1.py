#%%
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# %%
sns.get_dataset_names()

# %%
iris = sns.load_dataset('iris')

# %%
iris.head(3)

# %%
sns.heatmap(iris.corr())

# %%
sns.jointplot(data=iris, x='sepal_length', y='sepal_width', kind='kde', 
    fill=True)
    
# %%
sns.distplot(iris.sepal_length, kde=True, bins=20)

# %%
# .str.contains()
# .isin([])
# df.at
# df.append(df2, ignore_index=True, sort=False)
# concat, join, merge
# df.drop(index=xxx, columns=xxx)
# df.sort_values(by=col/lst of cols, ascending=bool/list of bools, inplace=bool)
# df.sort_index()
# df[col].sort_values()
# sorted()
# df[col].nlargest(n)
# df.nlargest(n, col)
# nsmallest
# apply, map, applymap, replace

# %%
survey_df = pd.read_csv("C://Users//singh//Downloads//survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("C://Users//singh//Downloads//survey_results_schema.csv", index_col='Column')

# %%
survey_df.head(3)

# %%
schema_df.head(3)

# %%
schema_df.loc['Respondent', 'QuestionText']

# %%
[col for col in survey_df.columns]

# %%
survey_df.isna().sum()

# %%
survey_df.notna().sum()

# %%
survey_df.loc[survey_df.Dependents.notnull(),:].groupby(by=['Country', 'Gender'])['CompTotal', 'ConvertedComp', 'Age'].agg(['median', 'count']).head(15)

# %%
survey_df.groupby(by='Country')['Gender'].get_group('India').value_counts(normalize=True)

# %%
survey_df.groupby(by='Country')['Gender'].apply(lambda x: x.value_counts())

# %%
survey_df.groupby(by='Country')['Gender', 'Sexuality'].agg('count')

# %%
survey_df.loc[survey_df.LanguageWorkedWith.str.contains('Python')]

# %%
survey_df['LanguageWorkedWith'].str.contains('Python', na=False, regex=True)

# %%
survey_df.loc[survey_df['LanguageWorkedWith'].str.contains('Python', na=False, regex=True), ['Country', 'Gender']]

# %%
survey_df.loc[survey_df.Country == 'India']['LanguageWorkedWith'].str.contains('Python').sum()

# %%
survey_df.loc[survey_df.Country == 'India']['LanguageWorkedWith'].str.contains('Python').value_counts(normalize=True)

# %%
survey_df.groupby(by='Country')['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').value_counts(normalize=True))

# %%
survey_df.groupby(by='Country')['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').value_counts(normalize=True)).loc['India']

# %%
country_uses_python = survey_df.groupby(by='Country')['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_all_method_1 = survey_df.groupby(by='Country')['LanguageWorkedWith'].count()
country_all_method_2 = survey_df['Country'].value_counts()

# %%
country_uses_python.head(3)

# %%
country_all_method_1.head(3)

# %%
country_all_method_2.head(3)

# %%
pd.concat([country_uses_python, country_all_method_1], sort=False, axis='columns')

# %%
pd.concat([country_uses_python, country_all_method_2], sort=False, axis='columns')

# %%
survey_df.loc[survey_df.Country == 'Afghanistan', 'LanguageWorkedWith'].count()

# %%
survey_df.loc[survey_df.Country == 'Afghanistan', 'LanguageWorkedWith'].isna().sum()

# %%
survey_df.loc[survey_df.Country == 'Afghanistan', 'LanguageWorkedWith'].shape

# %%
survey_df.loc[survey_df.Country == 'Afghanistan', 'LanguageWorkedWith'].str.contains('Python').value_counts()

# %%
survey_df.LanguageWorkedWith.str.contains('Python').value_counts()

# %%
# df.dropna(axis='index'/'columns', how='any'/'all', subset=list of col/s)
# df.replace()
# df.replace(to_replace=['Yes', 'No'], value=[True, False]).equals(df.map({'Yes':True, 'No':False}))

#Research
"""
In [124]: s = pd.Series([0, 1, 2, 3, 4])    
In [125]: s
Out[125]: 
0    0
1    1
2    2
3    3
4    4
dtype: int64

In [126]: s.replace({0: 5})
Out[126]: 
0    5
1    1
2    2
3    3
4    4
dtype: int64

In [129]: s.map({0: 'kitten', 1: 'puppy'}) 
Out[129]: 
0    kitten
1     puppy
2       NaN
3       NaN
4       NaN
dtype: object
"""

# %%
#df.fillna(0)
#series/df.dtypes
#nan is a float under the hood... so nan can only be converted to a float not an int
#series/df.astype

# %%
#read.csv arguement na_values=list of values to consider as nan values
#.unique, .nunique

# %%
#cont in part 2
# %%
