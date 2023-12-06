import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score


train_df = pd.read_csv("titanic_train.csv")
test_df = pd.read_csv("titanic_test.csv")

print(train_df.head(5))

train_id = train_df["PassengerId"].values
test_id = test_df["PassengerId"].values

all_df = train_df.append(test_df).set_index('PassengerId')
print(all_df.head(5))

# 데이터 전처리
all_df["Sex"] = all_df["Sex"].replace({"male": 0, "female": 1})
all_df["Age"].fillna(
    all_df.groupby("Pclass")["Age"].transform("mean"), inplace=True)
all_df["cabin_count"] = all_df["Cabin"].map(lambda x: len(x.split()) if type(x) == str else 0)

all_df.loc[all_df["Fare"].isnull(), "Fare"] = 12.415462
all_df["cabin_type"] = all_df["Cabin"].map(lambda x : x[0] if type(x) == str else "None")

del all_df["Cabin"]
del all_df["Name"]
del all_df["Ticket"]

Y = all_df["Survived"]
del all_df["Survived"]

X_df = pd.get_dummies(all_df)
X = X_df.values

X_train = X[:len(train_id)]
X_test = X[len(train_id):]
Y_train = Y[:len(train_id)]
Y_test = Y[len(train_id):]

minmax_scaler = MinMaxScaler()
minmax_scaler.fit(X_train)

X_train = minmax_scaler.transform(X_train)
X_test = minmax_scaler.transform(X_test)

test_accuracy = []
train_accuracy = []
for idx in range(3, 20):
    dt = DecisionTreeClassifier(min_samples_leaf=idx)
    acc = cross_val_score(dt, X_train, Y_train, scoring="accuracy", cv=5).mean()
    train_accuracy.append(accuracy_score(dt.fit(X_train, Y_train).predict(X_train), Y_train))
    test_accuracy.append(acc)

result = pd.DataFrame(train_accuracy, index=range(3, 20), columns=["train"])
result["test"] = test_accuracy

result.plot()
plt.show()
