# Student Performance Analyzer
- A Python-based data analysis project that analyzes student academic performance using Pandas and NumPy and visualizes key insights using Matplotlib.

## Project Overview
- The Student Performance Analyzer is a data analysis project designed to evaluate student academic performance based on marks, attendance, and demographic information.
- The project generates a dataset of 500 students and performs data cleaning, statistical analysis, performance evaluation, and data visualization.

## Objectives
- Analyze student marks across different subjects.
- Calculate total marks, percentage, and grades.
- Identify highest and lowest performing students.
- Find the best and weakest performing subjects.
- Analyze grade distribution.
- Study the relationship between attendance and percentage.
- Calculate statistical measures such as mean, median, and standard deviation.
- Visualize important findings using Matplotlib.

## Features
- Generates a synthetic dataset of 500 students.
- Performs data quality checks.
- Detects missing values and duplicate records.
- Calculates total marks and percentage.
- Assigns grades based on percentage.
- Identifies highest and lowest performing students.
- Displays the top 3 students.
- Provides grade-wise student distribution.
- Identifies the best and weakest subject.
- Calculates attendance vs percentage correlation.
- Performs statistical analysis using NumPy.
- Generates visualizations using Matplotlib.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- CSV data format

## Project Structure

```text
STUDENT PERFORMANCE ANALYZER/
│
├── charts/
│   ├── subject_average.png
│   ├── grade_distribution.png
│   ├── attendance_vs_percentage.png
│   └── top_student.png
│
├── data/
│   └── students.csv
│
├── src/
│   ├── main.py
│   ├── generate_data.py
│   ├── data_analysis.py
│   ├── numpy_analysis.py
│   ├── student_utils.py
│   └── visualization.py
│
├── README.md
├── requirements.txt
└── .gitignore

## Dataset
- The project uses a synthetic dataset containing 500 student records.

### Dataset Columns

- | Column | Description |
- |---|---|
- | Student_ID | Unique student identifier |
- | Name | Student name |
- | Gender | Student gender |
- | Age | Student age |
- | Attendance | Attendance percentage |
- | Math | Mathematics marks |
- | Science | Science marks |
- | English | English marks |
- | Computer | Computer marks |
- | Total_Marks | Total marks across subjects |
- | Percentage | Overall percentage |
- | Grade | Grade based on percentage |

### Analysis Performed
- The project performs the following analysis:

#### Data Quality Analysis
- Checked for missing values.
- Checked for duplicate records.
- Verified dataset dimensions.

### Academic Performance Analysis
- Calculated average, maximum, and minimum marks for each subject.
- Calculated total marks and overall percentage.
- Assigned grades based on percentage.
- Identified the highest and lowest performing students.
- Identified the top 3 students.

### Statistical Analysis
- Calculated mean percentage.
- Calculated median percentage.
- Calculated standard deviation.
- Calculated subject-wise mean, median, and standard deviation.
- Calculated the correlation between attendance and percentage.

#### Grade Analysis
- Calculated the number of students in each grade category.
- Calculated the number of passed and failed students.

## Visualizations
- The project generates four visualizations using Matplotlib:

1. Average Marks by Subject
- Compares the average performance of students across Math, Science, English, and Computer.

2. Grade Distribution
- Shows the number of students in each grade category.

3. Attendance vs Percentage
- A scatter plot showing the relationship between student attendance and overall percentage.

4. Top 5 Students
- Displays the five students with the highest overall percentages.

## Key Insights

- Based on the analysis of 500 students.
- The average overall percentage is 74.529%.
- Computer is the best-performing subject with an average score of 77.158.
- Math is the weakest-performing subject with an average score of 72.840.
- 488 students passed and 12 students failed based on the 50% passing threshold.
- The median overall percentage is 75.125%.
- The standard deviation of overall percentage is 12.272.
- The correlation between attendance and percentage is approximately 0.118, indicating a weak positive linear relationship in this synthetic dataset.
- Three students achieved a percentage of 100% in the analyzed dataset.

# How to Run

1. Clone or download the project
- Open the project folder in VS Code.

2. Create a virtual environment
- python -m venv venv

3. Activate the virtual environment
##### Windows
- venv\Scripts\activate

4. Install dependencies
- pip install -r requirements.txt

5. Generate the dataset
- python src/generate_data.py
- This generates a synthetic dataset of 500 students and saves it to:
- data/students.csv

6. Run the analyzer
- python src/main.py
- The program performs data analysis, statistical analysis, and generates visualizations.

##### Future Improvements

- Add an interactive Streamlit dashboard.
- Add student-wise search and filtering.
- Add gender-wise performance analysis.
- Add attendance categories.
- Add performance comparison between different age groups.
- Add export functionality for analysis reports.
- Add more interactive charts and dashboards.

# Student Performance Analyzer

- **Developed by:** Aditya Singh  
- **Technology:** Python, Pandas, NumPy, Matplotlib
- A Python-based data analysis project that analyzes student academic performance using Pandas and NumPy and visualizes key insights using Matplotlib.
