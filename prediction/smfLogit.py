import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from imblearn.under_sampling import RandomUnderSampler

from sklearn.model_selection import train_test_split

from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

dir_path = "E:/Design/论文/data/"
results_path = "result2.csv"

feat_labels = [
    "arousal", "valence", "dominance",
    "anger", "sadness", "joy", "love",
    "politeness",
    "in_arousal", "in_valence", "in_dominance",
    "in_anger", "in_sadness", "in_joy", "in_love",
    "in_politeness",
    "is_developer",
    "num_commits",
    "num_issues_created",
    "num_comments"
]

data = pd.read_csv(dir_path + results_path, encoding="utf-8")

#特征选择
X = data[feat_labels]

y = data["merged"]

#采样
rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)



# #将index保存到新的列中
# X_train['index'] = X_train.index
# X_test['index'] = X_test.index

#归一化所有特征
# X_train_scaled = scaler.fit_transform(X_train.drop('index', axis=1))
# X_test_scaled = scaler.transform(X_test.drop('index', axis=1))

#
# X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X_train.columns[:-1])
# X_train_scaled_df.index = X_train['index']
# X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X_test.columns[:-1])
# X_test_scaled_df.index = X_test['index']

# 选择需要归一化的指标
# cols_to_normalize = ["arousal", "valence", "dominance", "anger", "sadness", "joy", "love", "politeness", "in_arousal",
#      "in_valence", "in_dominance", "in_anger", "in_sadness", "in_joy", "in_love", "in_politeness"]
# #归一化，归一化前要保存index信息
# scaler = StandardScaler()
#
# X_train[cols_to_normalize] = scaler.fit_transform(X_train[cols_to_normalize])
# X_test[cols_to_normalize] = scaler.transform(X_test[cols_to_normalize])

X_train_scaled_df = X_train

train =  pd.merge(X_train_scaled_df, y_train, left_index=True, right_index=True)

# 逻辑回归建模
formula = 'merged ~ arousal+valence+dominance+anger+sadness+joy+love+politeness+in_arousal+in_valence+in_dominance+in_anger+in_sadness+in_joy+in_love+in_politeness+is_developer+num_commits+num_issues_created+num_comments'

#formula = 'merged ~ arousal+valence+dominance+in_arousal+in_valence+in_dominance+is_developer+num_commits+num_issues_created+num_comments'


# 设置pandas的显示选项，禁止科学计数法
lg = smf.glm(formula=formula, data=train
             , family=sm.families.Binomial(sm.families.links.logit())).fit()
#设置 pandas 输出格式选项
summary = lg.summary().tables[1]
#设置float_format属性为一个lambda函数，该函数将浮点数输出为小数点后5位的格式
print(summary)
np.set_printoptions(precision=20, suppress=True,threshold=np.inf)
odds_ratio = pd.DataFrame({'OR': lg.params.apply(lambda x: round(np.exp(x), 2))})
print(odds_ratio)

# 得到预测标签
y_pred = np.round(lg.predict(X_test))

auc = roc_auc_score(y_test, lg.predict(X_test))
print("auc:" + str(auc) )

from sklearn.metrics import classification_report

# 假设y_true和y_pred分别为真实标签和模型预测结果
report = classification_report(y_test, y_pred)

# 输出测试集中0和1各自的TN、FN、TP、FP
print(report)