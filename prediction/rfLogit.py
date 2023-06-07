import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from imblearn.under_sampling import EditedNearestNeighbours, RandomUnderSampler, TomekLinks, OneSidedSelection, \
    NeighbourhoodCleaningRule
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, Normalizer
from statsmodels.iolib.table import SimpleTable
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

dir_path = "E:/Design/"
results_path = "grouped_result.csv"

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
    "trinary", "binary", "scale", "Positive", "Negative",
    "Please",
    "Please_start",
    "HASHEDGE",
    "Indirect_btw",
    "Hedges",
    "Factuality",
    "Deference",
    "Gratitude",
    "Apologizing",
    "one_st_person_pl",
    "one_st_person",
    "one_st_person_start",
    "two_nd_person",
    "two_nd_person_start",
    "Indirect_greeting",
    "Direct_question",
    "Direct_start",
    "HASPOSITIVE",
    "HASNEGATIVE",
    "SUBJUNCTIVE",
    "INDICATIVE",
    "sentiCR",
    "EASTER",
    "senti4SD",
    "isDirectSentiment",
    "isDecoratedSentiment",
    "isAboutMe",
    "isJudgement"
]

data = pd.read_csv(dir_path + results_path, encoding="utf-8")

# 特征选择
X = data[feat_labels]

y = data["merged"]

# 采样
rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

X_train_scaled_df = X_train

train = pd.merge(X_train_scaled_df, y_train, left_index=True, right_index=True)

# 逻辑回归建模
# formula = 'merged ~ arousal+valence+dominance+anger+sadness+joy+love+politeness+in_arousal+in_valence+in_dominance+in_anger+in_sadness+in_joy+in_love+in_politeness+is_developer+num_commits+num_issues_created+num_comments+trinary+ binary+ scale+ Positive+ Negative+Please+Please_start+HASHEDGE+Indirect_btw+Hedges+Factuality+Deference+Gratitude+Apologizing+1st_person_pl+1st_person+1st_person_start+2nd_person+2nd_person_start+Indirect_greeting+Direct_question+Direct_start+HASPOSITIVE+HASNEGATIVE+SUBJUNCTIVE+INDICATIVE+sentiCR+EASTER+senti4SD'
formula = 'merged ~ arousal+valence+dominance+anger+sadness+joy+love+politeness+in_arousal+in_valence+in_dominance+in_anger+in_sadness+in_joy+in_love+in_politeness+is_developer+num_commits+num_issues_created+num_comments+Please+Please_start+HASHEDGE+Indirect_btw+Hedges+Factuality+Deference+Gratitude+Apologizing+one_st_person_pl+one_st_person+one_st_person_start+two_nd_person+two_nd_person_start+Indirect_greeting+Direct_question+Direct_start+HASPOSITIVE+HASNEGATIVE+SUBJUNCTIVE+INDICATIVE+sentiCR+EASTER+senti4SD+trinary+ binary+ scale+ Positive+ Negative+isDirectSentiment+ isDecoratedSentiment +isAboutMe +isJudgement'

# 设置pandas的显示选项，禁止科学计数法
lg = smf.glm(formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit())).fit()
# 设置 pandas 输出格式选项
summary = lg.summary().tables[1]
# 设置float_format属性为一个lambda函数，该函数将浮点数输出为小数点后5位的格式
print(summary)
np.set_printoptions(precision=20, suppress=True, threshold=np.inf)
odds_ratio = pd.DataFrame({'OR': lg.params.apply(lambda x: round(np.exp(x), 2))})
print(odds_ratio)

# 得到预测标签
y_pred = np.round(lg.predict(X_test))

auc = roc_auc_score(y_test, lg.predict(X_test))
print("auc:" + str(auc))

from sklearn.metrics import classification_report

# 假设y_true和y_pred分别为真实标签和模型预测结果
report = classification_report(y_test, y_pred)

# 输出测试集中0和1各自的TN、FN、TP、FP
print(report)
