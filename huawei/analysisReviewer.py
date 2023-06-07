import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import AutoDateLocator, DateFormatter

def analysisReviewer():
    csv_path = 'E:test.csv'
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False, encoding='gbk')
    data['code_review_create_timestamp'] = pd.to_datetime(data['code_review_create_timestamp'])
    data['merge_request_create_timestamp'] = pd.to_datetime(data['merge_request_create_timestamp'])

    start_date = datetime.datetime.strptime('20210101','%Y%m%d').date()
    end_date=datetime.datetime.strptime('20211231','%Y%m%d').date()

    create_staff_account_number = data['create_staff_account'].value_counts()

    project_id = '120771'
    create_account ='hwx578957'



    plt.plot_date(data[(data['create_staff_account'] == create_account)&(data['code_review_create_timestamp'].dt.date>=start_date)&(data['code_review_create_timestamp'].dt.date<=end_date)][['code_review_create_timestamp']],
                  data[(data['create_staff_account'] == create_account)&(data['code_review_create_timestamp'].dt.date>=start_date)&(data['code_review_create_timestamp'].dt.date<=end_date)][['positive']], fmt='b.')
    ax = plt.gca()

    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))  # 设置时间显示格式
    ax.xaxis.set_major_locator(AutoDateLocator(maxticks=24))  # 设置时间间隔

    plt.xticks(rotation=90, ha='center')
    label = [create_account]
    plt.legend(label, loc='upper right')

    plt.grid()

    ax.set_title(project_id + ' sentiment', fontproperties='SimHei', fontsize=14)
    ax.set_xlabel('time')
    ax.set_ylabel('positive')
    plt.savefig(project_id + " "+create_account + '.jpg')
    plt.show()
    #评审最多的五个
    reviewer_list = data[data['create_staff_account'] == create_account][['comment_user_account']].value_counts().head().index.values;
    for reviewer in reviewer_list:
        print(reviewer[0])
        plt.plot_date(data[(data['create_staff_account'] == create_account) & (data['comment_user_account'] == reviewer[0])&(data['code_review_create_timestamp'].dt.date>=start_date)&(data['code_review_create_timestamp'].dt.date<=end_date)][
                          ['code_review_create_timestamp']],
                      data[(data['create_staff_account'] == create_account) & (data['comment_user_account'] == reviewer[0])&(data['code_review_create_timestamp'].dt.date>=start_date)&(data['code_review_create_timestamp'].dt.date<=end_date)][['positive']], fmt='b.')

        ax = plt.gca()

        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))  # 设置时间显示格式
        ax.xaxis.set_major_locator(AutoDateLocator(maxticks=24))  # 设置时间间隔

        plt.xticks(rotation=90, ha='center')
        label = [create_account + "  "+ reviewer[0]]
        plt.legend(label, loc='upper right')

        plt.grid()

        ax.set_title(project_id + ' sentiment', fontproperties='SimHei', fontsize=14)
        ax.set_xlabel('time')
        ax.set_ylabel('positive')
        plt.savefig(project_id +" "+ create_account + " "+reviewer[0] +'.jpg')
        plt.show()





if __name__ == '__main__':
    analysisReviewer()