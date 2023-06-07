import pandas as pd


def dataAppend():
    indicator_path = "D:/Projects/Python/EASTER/data/gm_eclipse_PRNum.csv"
    indicator = pd.read_csv(indicator_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    #
    data_path = "E:/Design/经过处理提取的数据集/gm_eclipse.csv"
    data = pd.read_csv(data_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)


    data = pd.merge(data, indicator, how='inner', on='changeId')
    data.index = data.index + 1
    data = data.drop(['changeId'], axis=1)
    data.to_csv(data_path, index=True, index_label='ID', sep=',', encoding="utf_8_sig")


if __name__ == '__main__':
    dataAppend()

