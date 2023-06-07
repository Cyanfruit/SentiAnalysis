import pandas as pd

def dataHandle():
    prediction_path = "D:/Projects/Python/EASTER/data/gm_libreoffice_宽.csv"
    prediction = pd.read_csv(prediction_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    #prediction.rename(columns={'Overall': 'TEXT'}, inplace=True)
    #需要重命名列
    prediction.replace({"Overall": {0:1, 1:-1, 2:0}}, inplace=True)
    #去掉中立的数据
    prediction = prediction[(prediction['Overall']!=-1)]

    prediction.index = prediction.index + 1
    prediction.to_csv(prediction_path, index=True, index_label='ID', sep=',', encoding="utf_8_sig")
    prediction = pd.read_csv(prediction_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)

    data_path = "E:/Design/经过处理提取的数据集/gm_libreoffice.csv"
    data = pd.read_csv(data_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    #去掉未修改文件和修改数量大于10000的数据
    data = data[(data['churn'] != '')]
    # data['churn'] = data['churn'].astype(float)
    # data = data[(data['churn'] < 10000)]

    #去掉超过六天半的评审
    data = data[(data['timeDiff']>=0)]
    #data = data[(data['timeDiff'] < 96)]


    data = pd.merge(data, prediction, how='inner', on='ID')
    data.index = data.index + 1
    data = data.drop(['ID'], axis=1)
    data.to_csv(data_path, index=True, index_label='ID', sep=',', encoding="utf_8_sig")

if __name__ == '__main__':
    dataHandle()

    