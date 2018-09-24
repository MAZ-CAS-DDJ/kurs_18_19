#INSTALL
pip install pandas

#SET UP
import pandas as pd
import numpy as np                      #need this for NaN

#DISPLAY OPTIONS
pd.set_option("optionName", value)      #Change the behavior of displayed content in notebooks
    "display.max_rows"                  #the number of rows of a DataFrame
    "display.max_columns"               #The number of columns of a DataFrame
    "display.max_colwidth"              #The number of chars inside a column
    "display.float_format"              # something like "{:,.0f}".format

pd.options.display.max_rows             #to display the current settings

#DATA IN AND OUT
df = pd.read_csv("file.csv")
    nrows=59                            #to only get a number of rows
    na_values=["string1", "string2", ...] #to specify values to ignore
    dtype=str                           #treat everything as strings
    sep="\t"                            #for tab-delimited files
    error_bad_lines=False               #Ignore errors (i.e. too many fields on a line)
    header=None                         #use if csv has no header-row
    names=["id", "cat"]                 #specify column names to be used

df = pd.read_excel("file.xlsx")
    sheetname="name"                    #the name of the sheet inside excel
    skiprows=n                          #skip the first n rows
    names=list                          #use these column names

df.to_csv("file.csv")                   #save a DF into the specified csv
    index=False                         #don't save the index column

df.to_dict()                            #save dataframe as dictionary
    orient="records"/"list"/...         #way of constructing the dictionary

df.to_json()                            #save as json-string (almost like to_dict)
    orient="records"/"index"

#CONSTRUCTOR
df = pd.DataFrame(listofdics)           #create a DF from a list of dictionaries
    columns=["col1", "col2"]            #specify order of columns

df = pd.DataFrame(                      #other possibility
    "field1": val1, val2, val3
    "field2": val4, val5, val6
)

df = pd.DataFrame(                      #other possibility
    ['field1', value1, value2],
    ['field2', value1, value2]
)

s = pd.Series(dict)                     #construct a Series from a dict

#SERIES AND DATAFRAMES
.to_frame()                             #converts a series into a dataframe

#BASICS
?                                       #get help on a method ( e.g. type pd.head? )
NaN                                     #Placeholder for missing data
np.nan                                  #code for nan (need to import numpy as np)

#GET TABULAR DATA (DATAFRAME OBJECTS)
df                                      #represents whole table
df.field1                               #fetch only one column
df["field1"]                            #alternative notation
df[["field1", "field2"]]                #fetch several columns
df[condition]                           #only fetch rows where condition is true

#GET SINGLE ROW
df.loc[index]                           #get row at particular index
df.iloc[integer]                        #treat index as if it was a range of integers

#PROPERTIES OF DATAFRAME OBJECTS
.index                                  #A list of row-indices (usually numbers)
.columns                                #A list of column names
.dtypes                                 #A list of column datatypes
.shape                                  #A tuple specifying (rows, columns)
.values                                 #A matrix of the table without headers and row indices

#METHODS ON DATAFRAME OBJECTS - WHOLE DATASET
df.copy()                               #copy the dataframe (instead of just referencing it)

df.head(n)                              #only first n rows
df.tail(n)                              #only last n rows

df.set_index("field")                  #change the index-column to "field1"
    inplace=True                       #actually make the changes

df.insert(pos, "field1", values)        #insert new column "field1" at pos with values
df.pop("field1")                        #delete column "field1"
df.assign(newfield = df["field1"] ... ) #assign values to new column (original remains)

df.rename(columns=dict)                 #rename columns, using {'old1': 'new1', 'old2': 'new2'} as dict
    inplace=True
df.rename_axis("Name")                  #Rename the index column. Use 'None' to delete the index name
    inplace=True

df.pivot()                              #transform long data into wide data
    index='foo'
    columns='bar'
    values='baz'

df.melt()                               #transform wide data into long data

df.groupby("field1")                    #to initialize grouped output - need field & aggregate function
df.groupby(["field1", "field2"])        #groupby on two levels

df.unstack()                            #transform groupby-subrows into columns (useful to chart stacked bars)

df.sort_values("field1")                #sort values
    ascending=False                        #in descending order
    na_position="first"/"last"             #position of NaN values
df.sort_index()                         #sort not by values but by indexs

df.dropna()                             #get rid of NaNs, optional: in a subset
    subset="field1"                     #only apply on subset
    inplace=true                        #modify the original, not create a copy
    how="all"                           #only drop rows where all fields are NaN
df.fillna(value)                        #replace NaN's with other value
    inplace=true                        #modify the df itself, not in returned object

df.drop_duplicates()                    #gets rid of duplicate vlalues
    subset="field"                      #only consider certain fields (or list of fields)
    keep="first/last/False"             #which of the values to keep
    inplace=True/False                  #default = False

df.duplicated()                         #The duplicates (inverse of drop_dupclicated())
    subset="field"                      #only consider certain fields (or list of fields)
    keep="first/last/False"             #which of the values to keep

df.round({'field1': n, 'field2': m})    #round the numbers in particular columns

df.transpose()                          #switches row and columns over the whole dataset
df.T                                    #shorthand for dr.transpose()

df.dot(df2)                             #dot product of two dataframes

df.update(df2)                          #Update values in df with no-Nan values from df2

#COMBINE DATAFRAMES
df.merge(df2)                           #merge dataframe with other dataframe
    on="field"                          #fieldname(s) to match (if they have same name)
    left_on="df1-field"
    right_on="df2-field"                #specify on which fields to to the join
    left_index=True
    right_index=True                    #use the index to match
    how="inner/left/right/outer"        #just like in SQL

df.join(df2)                            #join a dataframe (with identical number of rows) to another

pd.concat(dflist)                       #adds all the dataframes in the list
    axis=1                              #add horizontally, not vertically
    ignore_index=True                   #construct new index, don't use existing one

#METHODS ON DATAFRAME OBJECTS - COMPARISONS

pd.isnull()                             #Built-in function to test for null on any value
pd.notnull()                            #same

df["field1"].isnull()                   #returns true if null
            .notnull()                  #opposite

df["field1"].str.contains("str")        #returns true if field1 contains the string str
    na=False                            #Avoid Error for NaN values
    regex=True/False                    #by default, regex can be included
    case=True/False                     #case sensitive or not, default True

df["field1"].isin(["str1", "str2"])     #returns true if field1 equals a value in the list
~df["field1"].isin(["str1", "str2"])     #returns true if field1 doesn't equal a value in the list

#METHODS ON DATAFRAME OBJECTS - ONLY ONE column
df["field1"].describe()                  #displays max, min, mean, etc

df["field"].value_counts()              #frequency of each value, in tabular form
    normalize=true                      #in percentages
    dropna=False                        #include NaN's in denominator
    ascending=True                      #Sort in inverse order

df["field1"].hist()                     #returns a graphical histogram
    bins=n                              #change number of bins to n
    bins=[n1, n2, n3, ...]              #set specific ranges

df["field1"].astype(int)                #convert to a type (int, str, float)
    errors="ignore"                     #ignore errors

df["field1"].replace("str1", "str2")    #replace stuff inside a string (use str.replace to replace parts inside the string)
    dictionary                          #uses key-value pairs in the dictionary to replace multiple values
    regex=True                          #use regex to find instances of str1

df["field1"].extract(regex)             #extracts a regex from the field
    expand=True                         #force return of a dataframe instead of a series
    .dropna()                           #to drop the NA values

df["field"].unique()                    #get a list of unique (distinct) values

pd.get_dummies(df["field"])             #Based on unique values in a field, create a set of dummy columns
    prefix="prefix"                     #Prefix to use before using unique values as column headers
    drop_first=True)

#METHODS ON DATAFRAME OBJECTS - ONLY ONE row
df.append(series/dataframe)             #adds the row, returns new object

df.drop(df[condition].index)            #delete rows from table based on condition
    inplace=True                        #Do it on the same object

#NUMERICAL FUNCTIONS
df.rolling(n, on="column")              #returns the rolling average of "column" as a DF
    min_periods=n                       #set number of periods to average over

df.column.pct_change()                  #calculates %-change between period t and t+1 (on single column or whole df)

df.column.agg(['func1', 'func2'])       #applies aggregate function like 'mean' etc. to column and spits out a dataframe


#ASSIGN FIELD VALUES DYNAMICALLY
df.loc[cond, "field"] = "value"         #sets "field" = "value" in all rows where "cond" is True

df.apply(function)                      #applies some function to the dataframe
    axis = 1                            #tells the function to treat the df in ROWS. default: COLUMNS

def function(x):                        #need to define the function

df["field1"] = df.apply(function)       #save the result in a new column

#METHODS ON DATAFRAME OBJECTS - AGGREGATE FUNCTIONS
.max()                      #maxiumum
.min()                      #minimum
.mean()                     #mean
.std()                      #standard deviation
.sum()                      #sum
.count()                    #count
.size()                     #useful for double-groupbys, similar to value_counts()
    axis=1                  #use all these functions not column-wise but row-wise


#DEALING WITH TIME
pd.to_datetime(df.column)                #Turn a string into a datetime. without args, leaves format unchanged
    format="format"                     #specify the format (e.g. "%Y-%m-%d") see: http://strftime.org/

.year                                   #get the year from a date-formatted column
.month                                  #---the month
.day                                    #---the day of the month
.dayofweek                              #---the day of the week

.dt.to_period('format')                 #get the number of elapsed days/months/years, etc

datetime.timedelta()                    #get a representation for a time interval
    days=n                                  #specify number of days

timedeldta.days                         #return number of days in a timedelta object
          .years                        # ----------------yers
          ...

df['YYYY']                              #select rows from that year
df['YYYY':'YYYY']                       #select range of years

df.resample('rule')                     #aggregate data so some specific time interval
                                        #see: https://stackoverflow.com/questions/17001389/pandas-resample-documentation/17001474#17001474

df.rolling(n)                           #aggregate with n neighbors. chain with .mean(), .sum() or other

df.column.apply(lambda (t): t.strftime('format')) #to transform a datetime col as string


#SQL-DATABASE HANDLING
pd.read_sql(query, conn)                #execute a SQL-query on a given connection
    index_col="column"                  #the column to be used as index
