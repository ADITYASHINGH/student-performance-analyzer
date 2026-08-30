import numpy as np


def percentage_statistics(df):

    print("\nOverall Percentage Statistics")

    mean_percentage = np.mean(df['Percentage'])
    median_percentage = np.median(df['Percentage'])
    std_percentage = np.std(df['Percentage'])

    print("Mean:", mean_percentage)
    print("Median:", median_percentage)
    print("Standard Deviation:", std_percentage)


def subject_statistics(df):

    subjects = ['Math', 'Science', 'English', 'Computer']

    print("\nSubject-wise Statistics")

    for subject in subjects:

        mean_marks = np.mean(df[subject])
        median_marks = np.median(df[subject])
        std_marks = np.std(df[subject])

        print(f"\n{subject}")
        print("Mean:", mean_marks)
        print("Median:", median_marks)
        print("Standard Deviation:", std_marks)