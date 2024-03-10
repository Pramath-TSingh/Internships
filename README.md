# Internships
Assignments



1. Import necessary libraries - The code begins by importing the necessary Python libraries - pandas for data manipulation, and datetime for handling date and time data.

2. Read the input CSV file - The `pd.read_csv()` function is used to read the input CSV file into a DataFrame, which is a two-dimensional tabular data structure with labeled axes (rows and columns).

3. Initialize an empty list for the output - An empty list named output is created to store the transformed data.

4. Iterate over each row in the input DataFrame - A for loop is used to iterate over each row in the input DataFrame. For each row, the following steps are performed.

5. Extract the employee code and manager employee code- The employee code and manager employee code are extracted from the current row.

6. Extract the dates of joining and exit- The dates of joining and exit are extracted from the current row and converted to datetime objects.

7. Extract the compensation details- The compensation details are extracted from the current row. The compensation amounts and their corresponding dates are stored in separate lists.

8. Extract the review details- The review details are extracted from the current row. The review scores and their corresponding dates are stored in separate lists.

9. Extract the engagement details- The engagement details are extracted from the current row. The engagement scores and their corresponding dates are stored in separate lists.

10. Combine all the dates and sort them- All the dates (joining, exit, compensation, review, and engagement dates) are combined into a single list and sorted in ascending order.

11. Iterate over each date- A for loop is used to iterate over each date in the sorted list of dates.

13. Concatenate all the DataFrames in the output list- The pd.concat() function is used to concatenate all the DataFrames in the output list into a single DataFrame.

14. Write the output DataFrame to a CSV file- The to_csv() function is used to write the output DataFrame to a CSV file.
