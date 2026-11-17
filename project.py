<<<<<<< HEAD

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create the dataset
df=pd.read_csv("students.csv")
print(df)

print("Original Dataset:")
print(df)


# 2. Introduce a missing value
df.loc[4, "Marks"] = float("nan")

print("\nMissing Values:")
print(df.isnull().sum())


# 3. Handle missing values using mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset After Filling Missing Values:")
print(df)


# 4. Check and remove duplicate records
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()


# 5. Sort students by marks (highest first)
print("\nStudents Sorted by Marks:")
print(df.sort_values("Marks", ascending=False))


# 6. Display the top 3 students
print("\nTop 3 Students:")
print(df.sort_values("Marks", ascending=False).head(3))


# 7. Filter students scoring above 80
print("\nStudents Scoring Above 80:")
print(df.loc[df["Marks"] > 80, ["Name", "Marks"]])


# 8. Filter students scoring between 70 and 90
print("\nStudents Scoring Between 70 and 90:")
print(
    df.loc[
        (df["Marks"] >= 70) & (df["Marks"] <= 90),
        ["Name", "Marks"]
    ]
)


# 9. Filter CSE students scoring at least 80
print("\nCSE Students Scoring At Least 80:")
print(
    df.loc[
        (df["Department"] == "CSE") & (df["Marks"] >= 80),
        ["Name", "Marks"]
    ]
)


# 10. Group students by department and calculate average marks
avg_marks = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(avg_marks)


# 11. Calculate department-wise total marks
print("\nTotal Marks by Department:")
print(df.groupby("Department")["Marks"].sum())


# 12. Calculate highest marks in each department
print("\nHighest Marks by Department:")
print(df.groupby("Department")["Marks"].max())


# 13. Calculate multiple statistics
print("\nDepartment-wise Statistics:")
print(
    df.groupby("Department")["Marks"].agg(
        ["sum", "mean", "min", "max", "count"]
    )
)


# 14. Count students in each department
print("\nNumber of Students by Department:")
print(df.groupby("Department")["Marks"].size())


# 15. Visualize average marks by department
plt.bar(avg_marks.index, avg_marks.values)

plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Department-wise Average Student Marks")

plt.show()

# Histogram: Distribution of student marks
plt.hist(df["Marks"],bins=10)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")

plt.show()


plt.scatter(df["Study_Hours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()

total_marks=df.groupby("Department")["Marks"].sum()
plt.bar(total_marks.index,total_marks.values)
plt.xlabel("Department")
plt.ylabel("Total marks")
plt.title("Total Marks by Department")
plt.show()

highest_marks=df.groupby("Department")["Marks"].max()
plt.bar(highest_marks.index,highest_marks.values)
plt.xlabel("Department")
plt.ylabel("Highest Marks")
plt.title("Highest Marks by department")
plt.show()

department_count=df["Department"].value_counts()

plt.pie(
    department_count.values,
    labels=department_count.index,
    autopct="%1.1f%%"
)
plt.title("Department-wise student distribution")
plt.show()

tests=["Test 1","Test 2","Test 3","Test 4"]
marks=[60,70,75,90]
plt.plot(tests,marks,marker="o")
plt.xlabel("Tests")
plt.ylabel("Marks")
plt.title("Student Performance over time")
plt.show()

needs_improvement=df.loc[
    df["Marks"]<75,
    ["Name","Department","Marks"]
]
print("Students Needing improvement:")
print(needs_improvement)

high_performers=df.loc[
    df["Marks"]>=90,
    ["Name","Department","Marks"]
]
print("High performing students:")
print(high_performers)

# correlation

correlation=df["Study_Hours"].corr(df["Marks"])
print("Correlation between study hours and marks:",correlation)
=======
import pandas as pd
df=pd.DataFrame({
    "Name":["anu","ajith","pranith","racchu","chammi"],
    "Marks":[90,99,98,97,96],
    "Attendance":[98,89,90,97,98]
})
print(df)

total_students = df.shape[0]
average_marks = df["Marks"].mean()
average_attendance = df["Attendance"].mean()

print("Total students:", total_students)
print("Average marks:", average_marks)
print("Average attendance:", average_attendance)

df["Result"]=df["Marks"].apply(
    lambda x:"excellent"if x>=80 
    else "needs improvement"
)
print(df["Result"].value_counts())

topper = df.loc[df["Marks"].idxmax(), "Name"]
lowest = df.loc[df["Marks"].idxmin(), "Name"]


print("Topper:", topper)
print("Lowest scorer:", lowest)
>>>>>>> 2ca3909b184d57679a994780824d207b20032d2b
