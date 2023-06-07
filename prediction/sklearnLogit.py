import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

dir_path = "E:/Design/论文/data/"
results_path = "result2.csv"
from sklearn.model_selection import train_test_split

data = pd.read_csv(dir_path + results_path, encoding="utf-8")


#特征选择
X = data[
    ["arousal", "valence", "dominance", "anger", "sadness", "joy", "love", "politeness", "in_arousal",
     "in_valence", "in_dominance", "in_anger", "in_sadness", "in_joy", "in_love", "in_politeness", "is_developer",
     "num_commits", "num_issues_created", "num_comments"]
]
y = data["merged"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


from sklearn.linear_model import LogisticRegression
# 构建模型
model = LogisticRegression(solver='liblinear')

# 拟合模型
model.fit(X_train, y_train)

# 预测结果
y_pred = model.predict(X_test)
##查看其对应的w
print('the weight of Logistic Regression:',model.coef_)

##查看其对应的w0
print('the intercept(w0) of Logistic Regression:',model.intercept_)

##在训练集和测试集上分布利用训练好的模型进行预测
train_predict=model.predict(X_train)
test_predict=model.predict(X_test)
from sklearn import metrics
##利用accuracy（准确度）【预测正确的样本数目占总预测样本数目的比例】评估模型效果
print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(y_train,train_predict))
print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(y_test,test_predict))

##查看混淆矩阵(预测值和真实值的各类情况统计矩阵)
confusion_matrix_result=metrics.confusion_matrix(test_predict,y_test)
print('The confusion matrix result:\n',confusion_matrix_result)

# 计算精确度、召回率、F1分数和AUC
precision = precision_score(y_test,test_predict)
recall = recall_score(y_test,test_predict)
f1 = f1_score(y_test,test_predict)
auc = roc_auc_score(y_test,test_predict)
print("precision:" + str(precision) )
print("recall:" + str(recall) )
print("f1:" + str(f1) )
print("auc:" + str(auc) )