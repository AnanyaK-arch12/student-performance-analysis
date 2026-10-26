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