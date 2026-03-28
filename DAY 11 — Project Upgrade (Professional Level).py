import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Age": [21,22,23,24,25,26,27,28,29,30],
    "Salary": [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000]
}

df = pd.DataFrame(data)

x = df [["Experience","Age"]]
y = df ["Salary"]

model = LinearRegression()
model.fit(x,y)

# user input
Exp = int(input("Enter your experience:"))
Ag = int(input("Enter your age:"))

prediction = model.predict([[Exp,Ag]])

print("This is your salary:",prediction)
