import csv
import pandas as pd

# tell top 10 operations to be done on a csv file using Python

# 1. Reading as a List
# 2. Reading as a Dictionary
# 3. Writing Rows
# 4. Reading into a DataFrame (Pandas)
# 5. Filtering Data
# 6. Selecting Columns
# 7. Aggregating and Summarising
# 8. Handling Custom Delimiters
# 9. Processing Large Files in Chunks
# 10. Saving to CSV (Pandas)




# 1. Reading as a List
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# 2. Reading as a Dictionary
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column_name'])





# 3. Writing Rows
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Header1', 'Header2'])
    writer.writerows([['Val1', 'Val2'], ['Val3', 'Val4']])



# 4. Reading into a DataFrame (Pandas)
df0 = pd.read_csv('data.csv')



# 5. Filtering Data
df1 = pd.read_csv('data.csv')
filtered_df = df1[df1['Price'] > 100]


# 6. Selecting Columns
# Loading only two columns
df3 = pd.read_csv('data.csv', usecols=['Name', 'Salary'])


# 7. Aggregating and Summarising
df4 = pd.read_csv('data.csv')
total_sales = df4['Sales'].sum()
avg_age = df4['Age'].mean()


# 8. Handling Custom Delimiters
df5 = pd.read_csv('data.csv', sep='\t')



# 9. Processing Large Files in Chunks
def process_this(chunk_local=None):
    print(chunk_local)
for chunk in pd.read_csv('huge_data.csv', chunksize=1000):
    process_this(chunk)



# 10. Saving to CSV (Pandas)
df6 = pd.read_csv('data.csv')
df6.to_csv('cleaned_data.csv', index=False)
