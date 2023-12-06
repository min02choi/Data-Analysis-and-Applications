from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


y_true = [1, 0, 1, 1, 0, 1]
y_pred = [0, 0, 1, 1, 0, 1]
confusion_matrix(y_true, y_pred)

tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print(tn, fp, fn, tp)

print("Accuracy Score: ", accuracy_score(y_true, y_pred))
print("Precision Score: ", precision_score(y_true, y_pred))
print("Recall Score: ", recall_score(y_true, y_pred))
print("F1 Score: ", f1_score(y_true, y_pred))
