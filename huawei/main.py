import six
import json
import paddlehub as hub
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, DateFormatter

def paddle():
    csv_path = 'E:/test.csv'
    acc = 0.00001
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)#读取数据
    dataList = data['text'].tolist();
    #data['code_review_create_timestamp'] = pd.to_datetime(data['code_review_create_timestamp'])
    #data['merge_request_create_timestamp'] = pd.to_datetime(data['merge_request_create_timestamp'])
    senti = anaSenti(dataList, acc)#训练
    df = pd.concat([data, senti], axis=1) #合并源数据和训练结果
    df.to_csv(csv_path, index=False, sep=',', encoding="utf_8_sig") #写入




# Load Senta-BiLSTM module
senta = hub.Module(name="senta_bilstm")

def anaSenti(test_text, acc):
    # 结果集：
    senti = []  # 创建空list
    positive = []
    negative = []
    # 指定模型输入
    input_dict = {"text": test_text}
    # 把数据喂给senta模型的文本分类函数
    results = senta.sentiment_classify(data=input_dict)
    # 遍历分析每个短文本
    # for index, text in enumerate(test_text):
    #    results[index]["text"] = text
    for index, result in enumerate(results):
        if six.PY2:
            print(json.dumps(results[index], encoding="utf8", ensure_ascii=False))
        else:
            # print('text: {},\t  predict: {}'.format(results[index]['text'], results[index]['positive_probs']))
            positive.append(results[index]['positive_probs'])
            negative.append(results[index]['negative_probs'])
            senti.append(translate(results[index]['positive_probs'], acc))
    dataFrame=pd.DataFrame({'positive': positive, 'negative': negative, 'result': senti})
    return dataFrame


def translate(pos_probs, acc):
    if pos_probs - 0.55 > acc:
        return 1
    elif pos_probs - 0.45 > acc:
        return 0
    else:
        return -1


if __name__ == '__main__':
    paddle()
