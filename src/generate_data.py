import numpy as np
import pandas as pd

np.random.seed(43)

num_students = 500 # number of student.

student_ids = np.arange(1001, 1001 + num_students) # student IDs

# Random student names
first_names = [
    "Aarav", "Aditya", "Rahul", "Rohan", "Amit",
    "Karan", "Arjun", "Vivek", "Ankit", "Ravi",
    "Akash", "Nikhil", "Vikas", "Rohit", "Varun",
    "Priya", "Neha", "Ananya", "Pooja", "Sneha",
    "Kavya", "Riya", "Simran", "Isha", "Aisha",
    "Nisha", "Shreya", "Muskan", "Tanya", "Divya"
]

last_names = [
    "Sharma", "Singh", "Verma", "Gupta", "Yadav",
    "Patel", "Kumar", "Mishra", "Agarwal", "Joshi",
    "Mehta", "Shah", "Pandey", "Tiwari", "Sinha",
    "Chauhan", "Srivastava", "Tripathi", "Saxena", "Dubey"
]

# Create all possible name combinations
name_pool = [
    f"{first} {last}"
    for first in first_names
    for last in last_names
]

# Select 500 unique names
names = np.random.choice(
    name_pool,
    size=num_students,
    replace=False
)

# Gender
gender = np.random.choice(
    ['M', 'F'],
    size=num_students
)

# Age
age = np.random.randint(
    18,
    25,
    size=num_students
)

# Attendance
attendance = np.random.randint(
    60,
    101,
    size=num_students
)

# Student ability
# Hidden variable used to generate
# realistic subject marks

ability = np.random.normal(
    70,
    12,
    size=num_students
)

# Generate subject marks
math = ability + np.random.normal(
    0, 8, size=num_students
)

science = ability + np.random.normal(
    2, 8, size=num_students
)

english = ability + np.random.normal(
    1, 7, size=num_students
)

computer = ability + np.random.normal(
    5, 7, size=num_students
)

# Attendance effect 
attendance_effect = (
    attendance - 60
) * 0.15

math = math + attendance_effect
science = science + attendance_effect
english = english + attendance_effect
computer = computer + attendance_effect

# 11. Keep Marks Between 0 and 100
math = np.clip(math, 0, 100)
science = np.clip(science, 0, 100)
english = np.clip(english, 0, 100)
computer = np.clip(computer, 0, 100)

# 12. Convert Marks to Integers
math = math.astype(int)
science = science.astype(int)
english = english.astype(int)
computer = computer.astype(int)


# 13. Create DataFrame
df = pd.DataFrame({
    'Student_ID': student_ids,
    'Name': names,
    'Gender': gender,
    'Age': age,
    'Attendance': attendance,
    'Math': math,
    'Science': science,
    'English': english,
    'Computer': computer
})


df.to_csv("data/students.csv",index=False)

print("Dataset generated successfully!")

print("\nFirst 10 Students:")
print(df[['Student_ID', 'Name', 'Gender', 'Age']].head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nBasic Statistics:")
print(df.describe())

print("\nDataset saved to:")
print("data/students.csv")