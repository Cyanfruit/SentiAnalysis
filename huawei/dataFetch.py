# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import pandas
import psycopg2

csv_path = 'D:\lw\pythonProject\paddleTest\mydada.csv'

## 加上字符集参数，防止中文乱码
dbconn=psycopg2.connect(
host="100.93.24.59",
database="wdo_dws",
user="wdo_dws_user_l50018418",
password="mZjRT8An3hVYkW9HaeUZS8vz",
port=5432
)

#sql语句
sql_code_review_comment = 'SELECT mr_id,comment_user_account,create_timestamp,code_project_id,comment_content FROM dwi.dwi_code_review_comment where code_project_id=\'129714\''
sql_code_merge_request = 'SELECT mr_title,create_staff_account,mr_id,create_timestamp FROM dwi.dwi_code_merge_request where (target_code_project_id = \'129714\' OR source_code_project_id = \'129714\')'

def dataFetch(dbconn, sql) -> pandas.DataFrame:
    # 利用pandas 模块导入mysql数据
    allData = pandas.read_sql(sql, dbconn)
    return allData

if __name__ == '__main__':
    code_review = dataFetch(dbconn,sql_code_review_comment)
    merge_request = dataFetch(dbconn,sql_code_merge_request)
    code_review.rename(columns={'create_timestamp': 'code_review_create_timestamp'},inplace=True)
    merge_request.rename(columns={'create_timestamp': 'merge_request_create_timestamp'},inplace=True)
    data = pandas.merge(merge_request,code_review,how='inner',on='mr_id')
    data.to_csv(csv_path, index=False, sep=',', encoding="utf_8_sig")