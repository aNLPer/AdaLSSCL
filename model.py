import numpy as np
from sklearn.metrics import label_ranking_average_precision_score

y_true=np.array([[0,0,0,0]])

y_pred=np.array([[0.9,0.4,0.9,0.5]])

out = label_ranking_average_precision_score(y_true=y_true, y_score=y_pred)

print(out)