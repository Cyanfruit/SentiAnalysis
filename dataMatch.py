import pandas as pd

# 地址
path_match = "E:/Design/经过处理提取的数据集/gm_eclipse_psm.csv"
path_data = "E:/Design/经过处理提取的数据集/gm_eclipse.csv"
data = pd.read_csv(path_data)
match = pd.read_csv(path_match)

data.replace({"Overall": {1:'negative',  0:'positive'}}, inplace=True)#根据工具修改列名

match_id = match['MatchId']
save_file = path_data.split(".")[0] + "所有数据.csv"
data[(data['ID'].isin(match_id))].to_csv(save_file, index=False, encoding="utf_8_sig")

save_file = path_data.split(".")[0] + "_干预组_消极.csv"
data[(data['ID'].isin(match_id))&(data['Overall']=='negative')].to_csv(save_file, index=False, encoding="utf_8_sig")

save_file = path_data.split(".")[0] + "_对照组_积极.csv"
data[(data['ID'].isin(match_id))&(data['Overall']=='positive')].to_csv(save_file, index=False, encoding="utf_8_sig")

