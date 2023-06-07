from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd

csv_path = 'D:/Projects/Java/SESSION/data/benchmark_data/AppReviews.csv'
data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False, encoding='utf-8')

actual = data['oracle']  # 真实的类别标签（data3是个dataframe，label是其中的一列）
predicted = data['Overall']  # 预测的类别标签

# 计算总的精度
acc = accuracy_score(actual, predicted)
print(acc)

# 计算混淆矩阵
#print(confusion_matrix(actual, predicted))

# 计算precision, recall, F1-score, support
class_names = ['negative', 'neutral', 'positive']
print(classification_report(actual, predicted,target_names=class_names))


p = precision_score(actual, predicted, average='micro')
p2 = precision_score(actual, predicted, average='macro')

r = recall_score(actual, predicted, average='micro')
r2 = recall_score(actual, predicted, average='macro')


f1score = f1_score(actual, predicted, average='micro')
f1score2 = f1_score(actual, predicted, average='macro')


print(p, p2)
print(r, r2)
print(f1score, f1score2)

'''
输出结果：
0.8969907407407407 0.614528783337003 0.9212413779093402
0.8969907407407407 0.6550877741326565 0.8969907407407407
0.8969907407407407 0.6041619746930149 0.8986671343868164
'''

'''
输出结果：
0.8969907407407407
array([[1032,    1,    0,    0,    0],
       [   3,  965,   17,    0,   15],
       [   0,   10,   42,    0,    6],
       [   0,   11,    3,    0,    0],
       [   0,   98,  103,    0,  286]])
'''