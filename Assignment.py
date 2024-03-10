# Importing the library

import pandas as pd

# Importing the Input data file

data = pd.read_csv('input.csv')
data.head()

# Checking the data

data.info()

# Creating the dataframe for inserting the processed  rows

process_cols = ['Employee Code', 'Manager Employee Code', 'Last Compensation', 'Compensation', 'Last Pay Raise Date', 'Variable Pay', 'Tenure in Org', 'Performance Rating', 'Engagement Score', 'Effective Date', 'End Date']
processed = pd.DataFrame([], columns=process_cols)
processed.info()

# Loop for iterating over ever employee

for ind, emp in data.iterrows():
  zero_interval = emp.iloc[:5].to_dict()
  intervals = emp.iloc[5:]

  common_column_name = [processed.columns[i] for i in range(processed.shape[1]) if processed.columns[i] in emp.index]
  row = {key: zero_interval[key] for key in common_column_name}
  row['Effective Date'] = zero_interval['Date of Joining']

  # Iterating over every compensation instance

  for i in range(1, 3):
    current_interval = intervals[[f'Compensation {i}', f'Compensation {i} date', f'Review {i}', f'Review {i} date', f'Engagement {i}',	f'Engagement {i} date']]

    if pd.notnull(current_interval[f'Compensation {i}']):
      row['Last Compensation'], row['Compensation'] = row['Compensation'], current_interval[f'Compensation {i}']