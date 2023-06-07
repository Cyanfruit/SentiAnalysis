import pickle
import pandas as pd

from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

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
    # "trinary",
    # "binary", "scale", "Positive", "Negative",
    # "Please",
    # "Please_start",
    # "HASHEDGE",
    # "Indirect_btw",
    # "Hedges",
    # "Deference",
    # "Gratitude",
    # "Apologizing",
    # "Indirect_greeting",
    # "Direct_question",
    # "Direct_start",
    # "HASPOSITIVE",
    # "HASNEGATIVE",
    # "SUBJUNCTIVE",
    # "one_st_person_pl",
    # "one_st_person",
    # "one_st_person_start",
    # "sentiCR",
    # "EASTER",
    # "senti4SD",
    # "isDirectSentiment",
    # "isDecoratedSentiment",
    # "isAboutMe",
    # "isJudgement"
]

dir_path = "E:/Design/论文/0/"

# 加载模型
with open(dir_path + 'rf_model.pkl', 'rb') as f:
    rf = pickle.load(f)

X_test_path = "X_test.csv"
y_test_path = "y_test.csv"
from sklearn.model_selection import train_test_split

X_test = pd.read_csv(dir_path + X_test_path, encoding="utf-8")
y_test = pd.read_csv(dir_path + y_test_path, encoding="utf-8")

# #特征选择
X = X_test[
    feat_labels
]

y = y_test['merged']

X_test = X
y_test = y

# 在测试集上进行预测
y_pred = rf.predict(X_test)

auc = roc_auc_score(y_test, y_pred)
print("auc:" + str(auc))

from sklearn.metrics import classification_report

# 假设y_true和y_pred分别为真实标签和模型预测结果
report = classification_report(y_test, y_pred, digits=3)

prob = rf.predict_proba(X_test)
print(prob)

# 输出测试集中0和1各自的TN、FN、TP、FP
print(report)
