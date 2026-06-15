Task 1: Daily Water Consumption
Create a line chart showing liters of water consumed during a week.

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
water = [2,3,2,4,3,5,4]

Requirements
* Create line chart
* Add title
* Add X label
* Add Y label
* Save chart as:

water_consumption.png


Task 2: Mobile Usage Hours

days = ["Mon","Tue","Wed","Thu","Fri"]
hours = [2,4,3,5,4]

Requirements
* Use line chart
* Show markers
* Enable grid

Task 3: Student Attendance Trend

weeks = ["Week1","Week2","Week3","Week4"]
attendance = [70,75,85,90]

Questions:
1. Which week has highest attendance?
2. Which week has lowest attendance?
Plot the chart.

Level 2: Bar Charts

Task 4: Subject Marks

subjects = ["Python","SQL","Statistics","English"]
marks = [88,92,75,80]

Create a bar chart.
Requirements
* Proper title
* X label
* Y label
* Save chart

Task 5: Monthly Expenses

expenses = {
    "Food": 5000,
    "Travel": 2500,
    "Shopping": 3000,
    "Bills": 2000
}

Create a bar chart.
Question:
Which category has highest expense?

Task 6: Department Employee Count

departments = ["HR","IT","Finance","Marketing"]
employees = [15,40,20,25]

Create bar chart.

Level 3: Scatter Plots

Task 7: Study Hours vs Marks

study_hours = [1,2,3,4,5,6]
marks = [40,50,60,70,80,90]

Create scatter plot.
Question:
What relationship do you observe?

Task 8: Attendance vs Marks

attendance = [60,70,80,90,95]
marks = [55,65,75,85,95]

Create scatter plot.

Task 9: Exercise vs Calories Burned

exercise_hours = [1,2,3,4,5]
calories = [150,250,350,450,550]

Create scatter plot.

Level 4: Data Analysis + Visualization

Task 10: Student Result Analysis
Create DataFrame:

import pandas as pd

students = {
    "Name":["Asha","Ravi","Kiran","John","Divya"],
    "Marks":[88,76,84,79,95]
}

df = pd.DataFrame(students)

Questions
1. Find average marks.
2. Find highest marks.
3. Find lowest marks.
4. Plot student marks.

Task 11: Employee Salary Dashboard

employees = {
    "Employee":["A","B","C","D","E"],
    "Salary":[35000,42000,50000,38000,60000]
}

Tasks
* Create DataFrame
* Find average salary
* Plot salary chart

Task 12: Product Sales Dashboard

sales = {
    "Product":["Laptop","Mouse","Keyboard","Monitor"],
    "Sales":[50,150,100,75]
}

Tasks
* Convert to DataFrame
* Plot bar chart
* Find best-selling product

Level 5: GroupBy Practice

Task 13: Branch-wise Average Marks

data = {
    "Student":["A","B","C","D","E","F"],
    "Branch":["CSE","ECE","CSE","EEE","ECE","CSE"],
    "Marks":[80,70,90,85,75,95]
}

Tasks
1. Create DataFrame
2. Calculate average marks branch-wise

df.groupby("Branch")["Marks"].mean()

1. Plot bar chart

Task 14: Department-wise Salary Analysis

data = {
    "Employee":["A","B","C","D","E"],
    "Department":["IT","HR","IT","Finance","HR"],
    "Salary":[50000,40000,60000,55000,45000]
}

Tasks
* Group by department
* Calculate average salary
* Plot chart
