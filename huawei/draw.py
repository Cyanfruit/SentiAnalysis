import pandas as pd
import matplotlib.pyplot as plt

def draw():
    csv_path = 'E:res.csv'
    data = pd.read_csv(csv_path, sep=',', header=0, skip_blank_lines=False, keep_default_na=False, encoding='gbk')
    data['code_review_create_timestamp'] = pd.to_datetime(data['code_review_create_timestamp'])
    data = data.set_index('code_review_create_timestamp')
    project_id = '129714'
    create_account = 'lwx949018'
    plt.rcParams['figure.figsize'] = (8.0,8.0)
    plt.subplot(1, 1, 1)
    data.plot(kind='line')
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

if __name__ == '__main__':
    draw()