import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df)
#
# print('Here is the data for the column of HP')
# print(df['HP'])
#
# print('Here is the data for the column of Speed')
# print(df['Speed'])
print('=======================================================')

#=================================================================
#READ DATA INTO PANDAS

##Read Headers
# print("Print out columns")
# print(df.columns)
#
# #Read each column
# print("Here are individual columns")
# print(df[['Name','Type 1','HP']])

#Read Each Row
# print("Here is Each Row")
# print(df.iloc[0:20])
#
# for index, row in df.iterrows():
#     print(index, row['Name'])

#Print Rows with Grass Types
# print(df.loc[df['Type 1'] == 'Grass'])

#Read a specific location (R,C)
# print('Here is a specified location')
# print(df.iloc[2,1])

#====================================================================
#Sort and Describe Data
# df.sort_values(['Type 1','HP'], ascending=[1,0])
#
# pd.set_option('display.width', 400)
# pd.set_option('display.max_columns', 10)
# pd.set_option('display.max_rows', df.shape[0]+1)
# print(df)

#===================================================================
#Make Changes to the Data

#Make New Column 'Total'
# df['Total'] = df['HP'] + df['Attack'] + df['Defense']+ df['Sp. Atk']+ df['Sp. Def']+ df['Speed']
# print(df)
#
# print(df.head(5))
#=================================================================

#Save Data
# df.to_csv('modified.csv')

#=================================================================
#Filtering Data

# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
#
# new_df.reset_index(drop=True, inplace=True)
# print(new_df)
#
# new_df.to_csv('filtered.csv')
#=================================================================

#Conditional Changes
modified_df = pd.read_csv("modified.csv")

modified_df.loc[modified_df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', df.shape[0]+1)
print(modified_df)