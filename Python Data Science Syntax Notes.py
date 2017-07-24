#Pandas

#setting change
import pandas as pd
pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
figsize(15, 5)


#DataFrame: collection of data series, 2 dimensional table of data
#Data Series: One two dimensional column of data, similar to python dict


#write to a csv:
df.to_csv('foo.csv')

#read from a csv:
pd.read_csv('test.csv')

#read csv without header
Cov = pd.read_csv("path/to/file.txt", sep='\t', header=None)
Cov.columns = ["Sequence", "Start", "End", "Coverage"]

#skip a row
pd.read_csv('test.csv', skiprows=[0])

#Save to a data frame
df = pd.read_csv('file.ext')

#remove whitespace

#select a column of data
df['column_name']

#select a specific by index
df.iloc[#]

#select a specific item in series
df['label']

#get first 5 rows of a dataframe
df[:5]

#get first 5 rows of a column
df['column_name'][:5]

#select 2 columns
df[['column_name', 'column_name']]

#most common types of data in a column
df_special = df['column_name'].value_counts()
df_special[:10]


#plot data - bar table
df_special[:10].plot(kind='bar')

#remove a column of data, delete by column label doesn't work unlabeled columns
df = df.drop('column_name',1)

#remove a column of data - keeping data inplace
df.drop('column_name', axis=1, inplace=True)

#remove a column of data by column number
df.drop(df.columns[[0,1,3]], axis=1)

#pop a column
df.pop('column_name')


#add a column of data, evaluating the data before adding
df.assign(expression)

#add column, data already exists
newcol = df['A']
df.assign(label=newcol)

#add a row of data, data already exists
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df.append(df2) #inputs the current index instead of existing
df.append(df2, ignore_index=True) #follow the existing index

#remove a row of data
df.drop(df.index[[1,3]], inplace=True)

#drop na
df.dropna()  #drop all rows that have any NaN values
df.dropna(how='all')     #drop only if ALL columns are NaN
df.dropna(thresh=2)   #Drop row if it does not have at least two values that are **not** NaN
df.dropna(subset=[1])   #Drop only if NaN in specific column