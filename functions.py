import numpy as np


def calculate_total(row):
    return row["Python"] + row["Maths"] + row["AI"]


def calculate_average(row):
    return np.mean([row["Python"], row["Maths"], row["AI"]])


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def check_result(row):
    if (
        row["Python"] >= 35
        and row["Maths"] >= 35
        and row["AI"] >= 35
    ):
        return "Pass"
    else:
        return "Fail"
    
def check_attendance(attendance):
    if attendance >= 75:
        return "Eligible"
    else:
        return "Low Attendance"