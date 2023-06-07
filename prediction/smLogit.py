import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


dir_path = "E:/Design/论文/data/"
results_path = "result.csv"
from sklearn.model_selection import train_test_split

data = pd.read_csv(dir_path + results_path, encoding="utf-8")

# 数据类型转换
data["politeness"] = data["politeness"].map({"impolite": 0, "polite": 1})
data["is_developer"] = data["is_developer"].replace({True: 1, False: 0})


#特征选择
X = data[
    ["arousal", "valence", "dominance", "anger", "sadness", "joy", "love", "politeness", "in_arousal",
     "in_valence", "in_dominance", "in_anger", "in_sadness", "in_joy", "in_love", "in_politeness", "is_developer",
     "num_commits", "num_issues_created", "num_comments"]
]
y = data["merged"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# #构建逻辑回归模型
X = sm.add_constant(X)  # 添加常数列
model = sm.Logit(y_train, X_train.astype('float'))
result = model.fit_regularized(method='l1', alpha=0.9)

print(result.summary())

# 获取模型参数
odds_ratio = pd.DataFrame({'OR': result.params.apply(lambda x: round(np.exp(x), 2))})
print(odds_ratio)