import pandas as pd

def dataHandle():
    csv_path = "E:/Design/经过处理提取的数据集/gm_libreoffice.csv"
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    # 在论文的基础上排除机器人构建
    # Bool1 = data.text.str.contains(
    #   "Build Started|Build Successful|Build Failed|Build Unstable|Uploaded patch set|Change has been successfully|was rebased|Build succeeded|Build failed|Build succeed|Passed using XenAPI driver|For rechecking only on the Microsoft Manila CI|Your change|Topic set to|Jenkins|Hudson|Bot|CI servers|I would prefer that|Change could not be merge|Change cannot be merged")

    # 只排除ci
    # Bool1 = data.text.str.contains(
    #     "cdskjcjdichsoicjoidsjvsdkjnvjk")

    #按照论文的格式筛选
    Bool1 = data.text.str.contains(
       "Build Started|Build Successful|Build Failed|Build Succeed|Jenkins|Hudson|Bot|CI servers")

    #data = data[~Bool]

    # 按照文本长度二次筛选
    #Bool2 = data.text.str.len() < 90
    #data = data[~(Bool1|Bool2)]
    data = data[~(Bool1)]

    #data.rename(columns={'hist_message': 'TEXT'}, inplace=True)
    data.to_csv(csv_path, index=False, sep=',', encoding="utf_8_sig")


    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False)
    data['text'] = data['text'].apply(lambda x: x.replace('\n', '').replace('\r', ''))


    data.index = data.index + 1

    data.to_csv(csv_path, index=True, index_label='ID',sep=',', encoding="utf_8_sig")


if __name__ == '__main__':
    dataHandle()
