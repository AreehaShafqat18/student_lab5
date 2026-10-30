
from src.dataset import make_df

df = make_df()

# 4.1 Select columns by name
print(df[["name", "salary"]].head(2))

# 4.2 Select a cell using its label
print(df.loc[1, "city"])

# 4.3 Select rows and columns by position
print(df.iloc[0:2, 0:2])

# 4.4 Filter rows using conditions
print(df[(df.salary > 50) & (df.city == "Karachi")])

# 4.5 Sort by salary (highest to lowest)
top = df.sort_values("salary", ascending=False)
print(top[["name", "salary"]].head(3))

# 4.6 Sort by city and age
by = df.sort_values(["city", "age"])
print(by[["city", "age"]])
