import matplotlib.pyplot as plt

def plot_subject_average(df):
    subjects = ['Math', 'Science', 'English', 'Computer']
    average_marks = df[subjects].mean()

    plt.bar(subjects,average_marks)
    plt.title("Data of student")
    plt.xlabel("Subjects")
    plt.ylabel("Average marks")
    plt.savefig('charts/subject_average.png')
    plt.show()

def plot_grade_distribution(df):

    grade_counts = df['Grade'].value_counts()

    plt.bar(grade_counts.index, grade_counts.values)
    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.savefig('charts/grade_distribution.png')
    plt.show()

def plot_attendance_vs_percentage(df):

    plt.scatter(df['Attendance'], df['Percentage'])
    plt.title("Attendance vs Percentage")
    plt.xlabel("Attendance")
    plt.ylabel("Percentage")
    plt.savefig('charts/attendance_vs_percentage.png')
    plt.show()

def plot_top_students(df):

    top_students = df.nlargest(5, 'Percentage')

    plt.bar(top_students['Name'], top_students['Percentage'])
    plt.title("Top 5 Students by Percentage")
    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.savefig('charts/top_student.png')
    plt.show()