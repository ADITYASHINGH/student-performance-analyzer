def basic_analysis(df):

    print("Missing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nDataset Shape:")
    print(df.shape)


def subject_analysis(df):

    subjects = ['Math', 'Science', 'English', 'Computer']

    avg_marks = df[subjects].mean()
    max_marks = df[subjects].max()
    min_marks = df[subjects].min()

    print("\nAverage Marks:")
    print(avg_marks)

    print("\nMaximum Marks:")
    print(max_marks)

    print("\nMinimum Marks:")
    print(min_marks)

    return avg_marks


def performance_analysis(df):

    highest_index = df['Percentage'].idxmax()
    lowest_index = df['Percentage'].idxmin()

    print("\nHighest Performing Student:")
    print(df.loc[highest_index, ['Name', 'Percentage', 'Grade']])

    print("\nLowest Performing Student:")
    print(df.loc[lowest_index, ['Name', 'Percentage', 'Grade']])

    average_percentage = df['Percentage'].mean()

    pass_count = (df['Percentage'] >= 50).sum()
    fail_count = (df['Percentage'] < 50).sum()

    
    print("\nAverage Percentage:", average_percentage)
    print("Number of Students Passed:", pass_count)

    top_students = df.nlargest(3, 'Percentage')

    print("\nTop 3 Students:")
    print(top_students[['Name', 'Percentage', 'Grade']])

    print("\nGrade-wise Student Count:")
    print(df['Grade'].value_counts())

    best_subject = df[['Math', 'Science', 'English', 'Computer']].mean().idxmax()
    weakest_subject = df[['Math', 'Science', 'English', 'Computer']].mean().idxmin()

    print("\nBest Performing Subject:", best_subject)
    print("Weakest Performing Subject:", weakest_subject)

    correlation = df['Attendance'].corr(df['Percentage'])

    print("\nAttendance vs Percentage Correlation:", correlation)