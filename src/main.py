import pandas as pd

from student_utils import calculate_grade
from data_analysis import basic_analysis, subject_analysis, performance_analysis
from numpy_analysis import percentage_statistics,subject_statistics
from visualization import plot_subject_average,plot_grade_distribution,plot_attendance_vs_percentage,plot_top_students

def main():

    df = pd.read_csv("data/students.csv")

    # Calculate Total Marks
    subjects = ['Math', 'Science', 'English', 'Computer']

    df['Total_Marks'] = df[subjects].sum(axis=1)

    # Calculate Percentage
    df['Percentage'] = df['Total_Marks'] / 4

    # Calculate Grade
    df['Grade'] = df['Percentage'].apply(calculate_grade)

    # Analysis
    basic_analysis(df)
    subject_analysis(df)
    performance_analysis(df)

    # NumPy Analysis
    percentage_statistics(df)
    subject_statistics(df)

    # Visualization
    plot_subject_average(df)
    plot_grade_distribution(df)
    plot_attendance_vs_percentage(df)
    plot_top_students(df)

if __name__ == "__main__":
    main()