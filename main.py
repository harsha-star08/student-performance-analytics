from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    check_result,
    check_attendance
)

import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

print("STUDENT PERFORMANCE ANALYTICS SYSTEM")

print(df)

print("\nTotal Students:", len(df))

print("\nDataset Information:")
df.info()
df["Total"] = df.apply(calculate_total, axis=1)

df["Average"] = df.apply(calculate_average, axis=1)
print("\nSTUDENT MARKS SUMMARY")
print(df[["Student_ID", "Name", "Total", "Average"]])


df["Grade"] = df["Average"].apply(calculate_grade)

df["Result"] = df.apply(check_result, axis=1)

print("\nSTUDENT GRADES AND RESULTS")
print(df[["Student_ID", "Name", "Average", "Grade", "Result"]])

print("\n========== CLASS STATISTICS ==========")

class_average = np.mean(df["Average"])
print("Class Average:", round(class_average, 2))

highest_average = df["Average"].max()
print("Highest Average:", highest_average)

top_student = df[df["Average"] == highest_average]
print("\nTop Performing Student:")
print(top_student[["Student_ID", "Name", "Average", "Grade"]])

lowest_average = df["Average"].min()
print("\nLowest Average:", lowest_average)

lowest_student = df[df["Average"] == lowest_average]
print("\nStudent with Lowest Average:")
print(lowest_student[["Student_ID", "Name", "Average", "Grade"]])

passed_students = (df["Result"] == "Pass").sum()
failed_students = (df["Result"] == "Fail").sum()

print("\nPassed Students:", passed_students)
print("Failed Students:", failed_students)

print("\n========== SUBJECT-WISE PERFORMANCE ==========")

python_avg = np.mean(df["Python"])
maths_avg = np.mean(df["Maths"])
ai_avg = np.mean(df["AI"])

print("Python Average:", round(python_avg, 2))
print("Maths Average:", round(maths_avg, 2))
print("AI Average:", round(ai_avg, 2))

subject_averages = {
    "Python": python_avg,
    "Maths": maths_avg,
    "AI": ai_avg
}

best_subject = max(subject_averages, key=subject_averages.get)

lowest_subject = min(subject_averages, key=subject_averages.get)

print("\nBest Performing Subject:", best_subject)
print("Lowest Performing Subject:", lowest_subject)

print("\nSubject Average Summary:")
for subject, average in subject_averages.items():
    print(subject, ":", round(average, 2))

print("\n========== ATTENDANCE ANALYSIS ==========")

average_attendance = np.mean(df["Attendance"])

print("Class Average Attendance:", round(average_attendance, 2), "%")



df["Attendance_Status"] = df["Attendance"].apply(check_attendance)

print("\nStudent Attendance Details:")
print(df[["Student_ID", "Name", "Attendance", "Attendance_Status"]])

low_attendance = df[df["Attendance"] < 75]

print("\nStudents with Attendance Below 75%:")

if len(low_attendance) > 0:
    print(low_attendance[["Student_ID", "Name", "Attendance"]])
else:
    print("All students have attendance of at least 75%.")

print("\nNumber of Students with Low Attendance:", len(low_attendance))

print("\n========== TOP 5 STUDENTS ==========")

top_students = df.sort_values(
    by="Average",
    ascending=False
).head(5)

print(top_students[["Student_ID", "Name", "Department", "Average", "Grade"]])

print("\n========== DEPARTMENT-WISE ANALYSIS ==========")

department_analysis = df.groupby("Department")["Average"].mean()

print("\nAverage Marks by Department:")
print(department_analysis.round(2))

best_department = department_analysis.idxmax()

print("\nBest Performing Department:", best_department)

lowest_department = department_analysis.idxmin()

print("Lowest Performing Department:", lowest_department)

print("\n========== GENERATING REPORT ==========")

report = df[
    [
        "Student_ID",
        "Name",
        "Department",
        "Python",
        "Maths",
        "AI",
        "Total",
        "Average",
        "Grade",
        "Result",
        "Attendance",
        "Attendance_Status"
    ]
]

report.to_csv("student_performance_report.csv", index=False)

print("Student performance report generated successfully!")
print("File Name: student_performance_report.csv")

