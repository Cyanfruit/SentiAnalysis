import pandas as pd
import numpy as np


def dataAggregate():
    csv_path = "E:/Design/经过处理提取的数据集/gm_eclipse.csv"
    data_path = "E:/Design/经过处理提取的数据集/每个patch的最后个comment.csv"
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    lastComment = data.groupby(['changeId', 'patchSetNum']).max('orderTime')
    var = data.loc[data['ID'].isin(lastComment['ID'])]

    var.reset_index(drop = True, inplace=True)
    var.index = var.index + 1
    var = var.drop(['ID'], axis=1)
    var.to_csv(data_path, index=True, index_label='ID', sep=',', encoding="utf_8_sig")

def count_vote(list1: list):
    if list1.count(0) > list1.count(1) :
        return 0
    else:
        return 1



def vote():
    csv_path = "E:/Design/经过处理提取的数据集/gm_eclipse.csv"
    data_path = "E:/Design/经过处理提取的数据集/投票决定保留的comment.csv"
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    vote_result = pd.DataFrame(data.groupby(['changeId', 'patchSetNum']).apply(lambda x: count_vote([i for i in x['PREDICTED']])))
    vote_result.rename(columns={0:'vote'}, inplace=True)
    lastComment = data.groupby(['changeId', 'patchSetNum']).min('orderTime')
    result = pd.merge(lastComment, vote_result, left_index=True, right_index=True)
    result.reset_index(drop=True, inplace=True)
    result.index = result.index + 1
    result = result.drop(['ID'], axis=1)
    result.to_csv(data_path, index=True, index_label='ID', sep=',', encoding="utf_8_sig")

if __name__ == '__main__':
    dataAggregate()
