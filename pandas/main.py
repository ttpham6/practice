# import pandas
import pandas as pd

# List of Tuples
employees = [('Stuti', 28, 'Varanasi', 20000),
            ('Saumya', 32, 'Delhi', 25000),
            ('Aaditya', 25, 'Mumbai', 40000),
            ('Saumya', 32, 'Delhi', 35000),
            ('Saumya', 32, 'Delhi', 30000),
            ('Saumya', 32, 'Mumbai', 20000),
            ('Aaditya', 40, 'Dehradun', 24000),
            ('Seema', 32, 'Delhi', 70000)
            ]

# Create a DataFrame object from list
df = pd.DataFrame(employees,
                columns =['Name', 'Age',
                        'City', 'Salary'])
# Show the dataframe
print(df)

# select the city column
result = df["City"]
print(result)


result1 = df[["Name", "Age", "Salary"]]
print(result1)


# Filter employees from Delhi
dehli_employees = df[df["City"] == "Delhi"]
print(dehli_employees)

# Filter based on condition of salary
high_salary_employees = [employee for employee in employees if employee[3] > 30000]
print(high_salary_employees)



older_employees = [employee for employee in employees if employee[1] >= 28 ]
print(older_employees)