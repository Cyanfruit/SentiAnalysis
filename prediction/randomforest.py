import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

from imblearn.under_sampling import RandomUnderSampler
import pickle

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
    "num_comments",
    "trinary",
    "binary", "scale", "Positive", "Negative",
    "Please",
    "Please_start",
    "HASHEDGE",
    "Indirect_btw",
    "Hedges",
    "Deference",
    "Gratitude",
    "Apologizing",
    "Indirect_greeting",
    "Direct_question",
    "Direct_start",
    "HASPOSITIVE",
    "HASNEGATIVE",
    "SUBJUNCTIVE",
    "one_st_person_pl",
    "one_st_person",
    "one_st_person_start",
    "sentiCR",
    "EASTER",
    "senti4SD",
    "isDirectSentiment",
    "isDecoratedSentiment",
    "isAboutMe",
    "isJudgement"
]

dir_path = "E:/Design/"
results_path = "grouped_result.csv"
from sklearn.model_selection import train_test_split

data = pd.read_csv(dir_path + results_path, encoding="utf-8")

# #特征选择
X = data[feat_labels]

y = data["merged"]

rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.3)

# 创建一个随机森林分类器对象
rfc = RandomForestClassifier(n_estimators=100, random_state=1)

# 在训练集上拟合分类器
rfc.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = rfc.predict(X_test)

auc = roc_auc_score(y_test, y_pred)
print("auc:" + str(auc))

from sklearn.metrics import classification_report

# 假设y_true和y_pred分别为真实标签和模型预测结果
report = classification_report(y_test, y_pred,digits=3)

# 输出测试集中0和1各自的TN、FN、TP、FP
print(report)

# 保存模型
with open('rf_model.pkl', 'wb') as f:
    pickle.dump(rfc, f)
