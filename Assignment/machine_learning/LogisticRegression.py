from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split


digit_dataset = datasets.load_digits()

X = digit_dataset["data"]
y = digit_dataset["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y)

logreg = LogisticRegression(max_iter=5000)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test).copy()
y_true = y_test.copy()

print("Confusion Matrix\n", confusion_matrix(y_true, y_pred))
print("Accuracy Score: ", accuracy_score(y_true, y_pred))
