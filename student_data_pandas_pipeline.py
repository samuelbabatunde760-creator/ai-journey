import pandas as pd

#Load data

df = pd.read_csv("raw_student.txt", header=None)

df.columns = ["Name", "Age", "Score1", "Score2", "Score3"]

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")


score_cols = ["Score1", "Score2", "Score3"]
for col in score_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

#Calculations
df["Average"] = df[score_cols].mean(axis=1)

def evaluate(avg):
    if pd.isna(avg): return "Data Missing"
    if avg >= 80: return "Excellent"
    elif avg >= 70: return "Good"
    else: return "Need Improvement"

df["Status"] = df["Average"].apply(evaluate)


df["MaxScore"] = df[score_cols].max(axis=1)
df["MinScore"] = df[score_cols].min(axis=1)
df["StdDev"] = df[score_cols].std(axis=1)

print("\n___ CLEANED STUDENT DATA (PANDAS VERSION) ___\n")
print(df[["Name", "Age", "Average", "Status"]])

# 7. Save
df.to_csv("processed_students.csv", index=False)