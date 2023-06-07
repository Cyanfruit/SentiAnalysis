import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import AutoDateLocator, DateFormatter

def analysisStaff():
    csv_path = 'E:test.csv'
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False, encoding='gbk')
    data['code_review_create_timestamp'] = pd.to_datetime(data['code_review_create_timestamp'])
    data['merge_request_create_timestamp'] = pd.to_datetime(data['merge_request_create_timestamp'])
    start_date = datetime.datetime.strptime('20201101', '%Y%m%d').date()
    end_date = datetime.datetime.strptime('20211231', '%Y%m%d').date()

    project_id = '129714_1'
    #评审最多的五个
    create_staff_account_number_list = data['create_staff_account'].value_counts().head(5).index

    for create_account in create_staff_account_number_list:
        #temp_path = 'D:\lw\pythonProject\paddleTest' + '\\' + create_account + '.csv'
        data_account = data[(data['create_staff_account'] == create_account)&(data['comment_user_account'] != create_account)]
        #data_account.to_csv(temp_path, index=False, sep=',', encoding="utf_8_sig")
        data_account['month'] = data['code_review_create_timestamp'].dt.month
        data_account['year'] = data['code_review_create_timestamp'].dt.year
        #data_account['strlen'] = data['comment_content'].apply(strLength)

        positive_mean = data_account.groupby(['year','month'])['positive'].mean()
        positive_std = data_account.groupby(['year', 'month'])['positive'].std()
        #length_mean = data_account.groupby(['year', 'month'])['strlen'].mean()
        plt.rcParams['figure.figsize'] = (16.0,8.0)

        plt.subplot(1, 2, 1)
        #plt.plot_date(data_account['code_review_create_timestamp'],data_account['positive'], fmt='b.')
        plt.plot_date(data[(data['create_staff_account'] == create_account) & (
                    data['code_review_create_timestamp'].dt.date >= start_date)][
                          ['code_review_create_timestamp']],
                      data[(data['create_staff_account'] == create_account) & (
                                  data['code_review_create_timestamp'].dt.date >= start_date)][['positive']],
                      fmt='b.')
        ax = plt.gca()
        ax.xaxis.set_major_formatter(DateFormatter('%Y-%m'))  # 设置时间显示格式
        ax.xaxis.set_major_locator(AutoDateLocator(maxticks=24))  # 设置时间间隔
        ax.set_title(project_id + ' sentiment', fontproperties='SimHei', fontsize=14)
        ax.set_xlabel('time')
        ax.set_ylabel('sentiment_value')
        plt.xticks(rotation=90, ha='center')
        label = [create_account]
        plt.legend(label, loc='upper right')
        plt.grid()

        plt.subplot(1, 2, 2)
        positive_mean[5:].plot(kind = 'line')
        ax = plt.gca()
        ax.set_title(project_id + ' mean', fontproperties='SimHei', fontsize=14)
        ax.set_xlabel('time')
        ax.set_ylabel('sentiment_value')
        plt.xticks(rotation=90, ha='center')
        label = [create_account]
        plt.legend(label, loc='upper right')
        plt.grid()


        # plt.subplot(1, 3, 3)
        # positive_std.plot(kind='line')
        # ax = plt.gca()
        # ax.set_title(project_id + ' std', fontproperties='SimHei', fontsize=14)
        # ax.set_xlabel('time')
        # ax.set_ylabel('std_value')
        # plt.xticks(rotation=90, ha='center')
        # label = [create_account]
        # plt.legend(label, loc='upper right')
        # plt.grid()

        # plt.subplot(2, 2, 4)
        # length_mean.plot(kind='line')
        # ax = plt.gca()
        # ax.set_title(project_id + ' str_length', fontproperties='SimHei', fontsize=14)
        # ax.set_xlabel('time')
        # ax.set_ylabel('str_length')
        # plt.xticks(rotation=90, ha='center')
        # label = [create_account]
        # plt.legend(label, loc='upper right')
        # plt.grid()


        plt.savefig(project_id +" "+ create_account +'.jpg')
        plt.show()

def strLength(string):
    return len(string)


if __name__ == '__main__':
    analysisStaff()