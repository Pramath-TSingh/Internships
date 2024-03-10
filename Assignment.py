import pandas as pd
from datetime import datetime, timedelta

# Read the input CSV file
df = pd.read_csv('input.csv')

# Create an empty list for the output
output = []

# Iterate over each row in the input DataFrame
for idx, row in df.iterrows():
    #Extract the employee code and manager employee code
    emp_code = row['Employee Code']
    mgr_emp_code = row['Manager Employee Code']

    # Extract the dates of joining and exit
    doj = datetime.strptime(row['Date of Joining'], '%Y-%m-%d')
    doe = datetime.strptime(row['Date of Exit'], '%Y-%m-%d') if pd.notnull(row['Date of Exit']) else datetime(2100, 1, 1)

    # Extract the compensation details
    comp = [row['Compensation'], row['Compensation 1'], row['Compensation 2']]
    comp_dates = [doj, datetime.strptime(row['Compensation 1 date'], '%Y-%m-%d') if pd.notnull(row['Compensation 1 date']) else None, datetime.strptime(row['Compensation 2 date'], '%Y-%m-%d') if pd.notnull(row['Compensation 2 date']) else None]

    # Extract the review details
    reviews = [row['Review 1'], row['Review 2']]
    review_dates = [datetime.strptime(row['Review 1 date'], '%Y-%m-%d') if pd.notnull(row['Review 1 date']) else None, datetime.strptime(row['Review 2 date'], '%Y-%m-%d') if pd.notnull(row['Review 2 date']) else None]

    # Extract the engagement details
    engagements = [row['Engagement 1'], row['Engagement 2']]
    engagement_dates = [datetime.strptime(row['Engagement 1 date'], '%Y-%m-%d') if pd.notnull(row['Engagement 1 date']) else None, datetime.strptime(row['Engagement 2 date'], '%Y-%m-%d') if pd.notnull(row['Engagement 2 date']) else None]

    # Combine all the dates and sort them
    all_dates = sorted(filter(None, [doj, doe] + comp_dates + review_dates + engagement_dates))

    # Iterate over each date
    for i in range(len(all_dates) - 1):
        # Determine the effective date and end date
        eff_date = all_dates[i]
        end_date = all_dates[i + 1] - timedelta(days=1)

        #Determine the compensation, revsew, and engagement for this period
        period_comp = next((comp[j] for j in reversed(range(len(comp_dates))) if comp_dates[j] and comp_dates[j] <= eff_date), None)
        period_review = next((reviews[j] for j in reversed(range(len(review_dates))) if review_dates[j] and review_dates[j] <= eff_date), None)
        period_engagement = next((engagements[j] for j in reversed(range(len(engagement_dates))) if engagement_dates[j] and engagement_dates[j] <= eff_date), None)

        # Append this periods data to the output list
        output.append(pd.DataFrame({
            'Employee Code': [emp_code],
            'Manager Employee Code': [mgr_emp_code],
            'Last Compensation': [period_comp],
            'Compensation': [period_comp],
            'Last Pay Raise Date': [comp_dates[-1] if comp_dates[-1] and comp_dates[-1] <= eff_date else None],
            'Variable Pay': [0],  # Variable Pay is always 0
            'Tenure in Org': [None],  # Tenure in Org is always None
            'Performance Rating': [period_review],
            'Engagement Score': [period_engagement],
            'Effective Date': [eff_date.strftime('%Y-%m-%d')],
            'End Date': [end_date.strftime('%Y-%m-%d')]
        }))

# Concatenate all the DataFrames in the output list
output = pd.concat(output, ignore_index=True)

# Write the output DataFrame to a CSV file
output.to_csv('output.csv', index=False)
