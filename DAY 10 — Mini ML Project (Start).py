import pandas as pd
from sklearn.linear_model import LinearRegression

# dataset (thoda bada)
data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

# user input
exp = int(input("Enter Experience: "))

prediction = model.predict([[exp]])

print("Predicted Salary:", prediction)