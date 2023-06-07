import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import AutoDateLocator, DateFormatter

def analysisRatio():
    csv_path = 'E:test.csv'
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False, encoding = 'gbk')
    data['code_review_create_timestamp'] = pd.to_datetime(data['code_review_create_timestamp'])
    data['merge_request_create_timestamp'] = pd.to_datetime(data['merge_request_create_timestamp'])

    project_id = '129714'
    #评审最多的五个
    create_staff_account_number_list = data['create_staff_account'].value_counts().head(10).index

    for create_account in create_staff_account_number_list:
        data_account = data[(data['create_staff_account'] == create_account)&(data['comment_user_account'] != create_account)]
        # data_account['month'] = data['code_review_create_timestamp'].dt.month
        # data_account['year'] = data['code_review_create_timestamp'].dt.year
        # data_account['week'] = data['code_review_create_timestamp'].dt.week
        #data_account['strlen'] = data['comment_content'].apply(strLength)
        #data_account = data_account[(data_account['strlen'] >= 10)]

        #大于和小于的统计密度
        positive_res = data_account[(data_account['result'] == 1)][['code_review_create_timestamp','result']]
        positive_res['code_review_create_timestamp'] = pd.to_datetime(positive_res['code_review_create_timestamp'])
        positive_res_count = positive_res.set_index('code_review_create_timestamp').resample('MS').count()
        positive_res_count = positive_res_count[(positive_res_count['result'] >= 10)]

        negative_res = data_account[(data_account['result'] == -1)][['code_review_create_timestamp','result']]
        negative_res['code_review_create_timestamp'] = pd.to_datetime(negative_res['code_review_create_timestamp'])
        negative_res_count = negative_res.set_index('code_review_create_timestamp').resample('MS').count()
        negative_res_count = negative_res_count[(negative_res_count['result'] >= 10)]
        res_temp = pd.merge(positive_res_count, negative_res_count,how='inner', on='code_review_create_timestamp')
        res = res_temp['result_x']/res_temp['result_y']
        if res.shape[0] >= 8:
            plt.rcParams['figure.figsize'] = (8.0,8.0)
            plt.subplot(1, 1, 1)
            restemp = res[1:10]
            res.plot(kind='line')
            ax = plt.gca()
            ax.set_title(project_id + ' pos/neg ratio', fontproperties='SimHei', fontsize=14)
            ax.set_xlabel('time')
            ax.set_ylabel('pos/neg')
            plt.xticks(rotation=90, ha='center')
            label = [create_account]
            plt.legend(label, loc='upper right')
            plt.grid()


            plt.savefig(project_id +" "+ create_account +'.jpg')
            plt.show()

def strLength(string):
    return len(string)


if __name__ == '__main__':
    analysisRatio()